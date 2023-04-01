from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@db/db"
db.init_app(app)

# print(engine.connect())
# cursor = db.get_db().cursor()
