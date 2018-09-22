from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from app.account_entity import AccountEntity

def db_init():
    db.create_all()


def add_data(object_data):
    db.session.add(object_data)
    db.session.commit()


def query_data(object_data):
    return object_data.query().all




