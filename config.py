from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config('SQLALCHEMY_DATABASE_URI') = "sqlite:///test16HW.db"


db = SQLAlchemy(app)


