from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

db = MySQL()
db.init_app(app)
