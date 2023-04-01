from sqlalchemy.sql import text
from flask import jsonify, Blueprint

from app import app, db

views = Blueprint('views', __name__)


@app.get('/home/')
def home():
    results = db.session.execute(text('select * from Company'), {})
    # print([result for result in results])
    print("ADSasdas")
    
    return jsonify([result[1] for result in results])
