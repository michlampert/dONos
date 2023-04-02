from sqlalchemy.sql import text
from flask import jsonify, request

from setup import app, db
from queries import get_company_id, get_leaderboard


@app.get('/home/')
def home():
    results = db.session.execute(text('select * from Company'), {})
    # print([result for result in results])
    print("ADSasdas")
    
    return jsonify([result[1] for result in results])


@app.get('/me/')
def get_me():
    employee_id = request.args.get('id')

    results = db.session.execute(
        text("select Name from Employee where EmployeeID = :employee_id"),
        {'employee_id': employee_id}
    ).fetchone()

    return jsonify({
        'name': results[0]
    })
    


@app.post('/company/add/')
def add_company():
    company_name = request.json.get('name')
    if not company_name:
        return jsonify(success=False)

    db.session.execute(text("insert into Company (Name) values (:name)"), {
        'name': company_name
    })
    db.session.commit()

    return jsonify(success=True)


@app.post('/employee/add')
def add_employee():
    name = request.json.get('name')
    company_id = request.json.get('company_id')

    db.session.execute(
        text(
            "insert into Employee (Name, CompanyID)"
            " values (:name, :company_id)"
        ), {
            'name': name,
            'company_id': company_id
    })
    db.session.commit() 

    return jsonify(success=True)


@app.get('/employee/')
def get_employees():
    company_id = request.args.get('company_id')

    results = db.session.execute(
        text("select EmployeeID, Name from Employee where CompanyID = :company_id"),
        {'company_id': company_id}
    )
    return [{
        'id': result[0],
        'name': result[1]
    } for result in results]


@app.get('/leaderboard/')
def get_leaderboard():
    company_id = request.args.get('company_id')

    results = db.session.execute(
        text("select t1.Name, pos, neg from Employee as b"
             " join (select Name, SUM(Score) as pos from Employee"
             "     left join Donos on Donor = EmployeeID"
             "     where CompanyID = :company_id group by Name) t1 on t1.Name = b.Name"
             " left join (select Name, SUM(Score) as neg"
             " from Employee join Donos on Receiver = EmployeeID"
             " where CompanyID = :company_id group by Name) t2 on"
             " t1.Name = t2.Name;"
             ),
        {'company_id': company_id}
    )
    sorted_results = sorted(results, key=lambda x: - int(x[1] or 0) + int(x[2] or 0))
    return [{
        'name': result[0],
        'points':{
            "plus": result[1] or 0,
            "minus": result[2] or 0
        }
    } for result in sorted_results]
    


@app.post('/donos/add')
def add_donos():
    content = request.json.get('content')
    donor = request.json.get('donor_id')
    receiver = request.json.get('receiver_id')
    image = request.json.get('image')

    db.session.execute(
        text("insert into Donos (Content, Donor, Receiver, status, score, image) "
             "values (:content, :donor, :receiver, 'waiting', 0, :image)"), 
        {
            'content': content, 'donor': donor, 'receiver': receiver, 'image': image
        }
    )
    db.session.commit() 

    return jsonify(success=True)


@app.post('/donos/<id>/accept')
def accept_donos(id: int):
    db.session.execute(
        text("update Donos set Status = 'accepted', Score = 15 where DonosID = :id"), 
        {
            'id': id
        }
    )
    db.session.commit() 

    return jsonify(success=True)


@app.post('/donos/<id>/reject')
def reject_donos(id: int):
    db.session.execute(
        text("update Donos set Status = 'rejected', Score = 0 where DonosID = :id"), 
        {
            'id': id
        }
    )
    db.session.commit() 

    return jsonify(success=True)


@app.post('/donos/<id>/super')
def super_donos(id: int):
    db.session.execute(
        text("update Donos set Status = 'accepted', Score = 25 where DonosID = :id"), 
        {
            'id': id
        }
    )
    db.session.commit() 

    return jsonify(success=True)


@app.get('/donos/')
def get_donos():
    company_id = request.args.get('company_id')

    results = db.session.execute(
        text("select DonosID, Content, d.Name as dName, r.Name as rName, Image"
             " from Donos join Employee as d on d.EmployeeID = Donor"
             " join Employee as r on r.EmployeeID = Receiver"
             " where Status = 'waiting' and d.CompanyID = :company_id;"),
        {'company_id': company_id}
    )
    results = list(results)
    return [{
        'id': result[0],
        'content': result[1],
        'donor_name': result[2],
        'receiver_name': result[3], 
        'image': result[4]
    } for result in results]


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
