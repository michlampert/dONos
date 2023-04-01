from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()
app = Flask(__name__)
CORS(app)

app.config["CORS_ORIGINS"] = ["*", "http://localhost:3000"]
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@172.27.0.2/db"
db.init_app(app)
