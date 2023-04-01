from app import app, db
from sqlalchemy.sql import text
from flask import jsonify


@app.get('/home/')
def home():
    results = db.session.execute(text('select * from Company'), {})
    print(list(results)[0])
    print([result for result in results])
    print("ADSasdas")
    
    return jsonify([result[1] for result in results])


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
