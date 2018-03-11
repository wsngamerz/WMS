import logging

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class DB:
    def __init__(self, config):
        logging.info("Initialising Databases")

class Main(db.Model):
    __bind_key__ = "main"

class User(db.Model):
    __bind_key__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
