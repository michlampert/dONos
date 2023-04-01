from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import jsonify, request


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@db/db"
db.init_app(app)


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
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    db.session.execute(
        text(
            "insert into Employee (FirstName, LastName) values (:first_name, :last_name)"
        ), {
            'first_name': first_name,
            'last_name': last_name
    })    

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
