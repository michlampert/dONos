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
        text("select FirstName, LastName from Employee where EmployeeID = :employee_id"),
        {'employee_id': employee_id}
    ).fetchone()

    return jsonify({
        'name': results[0] + " " + results[1]
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
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    company_id = request.json.get('company_id')

    db.session.execute(
        text(
            "insert into Employee (FirstName, LastName, CompanyID)"
            " values (:first_name, :last_name, :company_id)"
        ), {
            'first_name': first_name,
            'last_name': last_name,
            'company_id': company_id
    })
    db.session.commit() 

    return jsonify(success=True)


@app.get('/leaderboard/')
def get_leaderboard():
    company_id = request.args.get('company_id')

    results = db.session.execute(
        text("select t1.FirstName, t1.LastName, pos, neg from"
             " (select FirstName, LastName, SUM(Score) as pos from Employee"
             "     join Donos on Donor = EmployeeID"
             "     where CompanyID = :company_id group by FirstName, LastName) t1"
             " join (select FirstName, LastName, SUM(Score) as neg"
             " from Employee join Donos on Receiver = EmployeeID"
             " where CompanyID = :company_id group by FirstName, LastName) t2 on"
             " t1.FirstName = t2.FirstName and t1.LastName = t2.LastName;"),
        {'company_id': company_id}
    )

    return [{
        'name': result[0] + " " + result[1],
        'points':{
            "plus": result[2],
            "minus": result[3]
        }
    } for result in results]
    


@app.post('/donos/add')
def add_donos():
    content = request.json.get('content')
    donor = request.json.get('donor_id')
    receiver = request.json.get('receiver_id')

    db.session.execute(
        text("insert into Donos (Content, Donor, Receiver, status) "
             "values (:content, :donor, :receiver, 'waiting')"), 
        {
            'content': content, 'donor': donor, 'receiver': receiver
        }
    )
    db.session.commit() 

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
