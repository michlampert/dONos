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


@app.post('/leaderboard/add')
def add_leaderboard():
    comapny_name = request.json.get("name")

    company_id = get_company_id(comapny_name)

    db.session.execute(
        text("insert into Leaderboard (CompanyID) values (:company_id)"), 
        {'company_id': company_id}
    )
    db.session.commit() 

    return jsonify(success=True)


@app.post('/donos/add')
def add_donos():
    content = request.json.get('content')
    donor = request.json.get('donor_id')
    receiver = request.json.get('receiver_id')
    leaderboard = get_leaderboard(request.json.get('company_id'))

    db.session.execute(
        text("insert into Donos (Content, Donor, Receiver, LeaderboardID, status) "
             "values (:content, :donor, :receiver, :leaderboard, 'waiting')"), 
        {
            'content': content, 'donor': donor, 
            'receiver': receiver, 'leaderboard': leaderboard
        }
    )
    db.session.commit() 

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
