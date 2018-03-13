import logging

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ServerSettings(db.Model):
    __bind_key__ = "main"
    __tablename__ = "serverSettings"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    category = db.Column("category", db.String(64))
    value = db.Column("value", db.Text)
    description = db.Column("description", db.Text)

# Tables for the Users Database
class User(db.Model):
    __bind_key__ = "users"
    __tablename__ = "user"
    id = db.Column("userID", db.Integer, primary_key=True)
    username = db.Column("username", db.String(255), unique=True)
    firstName = db.Column("firstName", db.String(255))
    lastName = db.Column("lastName", db.String(255))
    fullName = db.column_property(firstName + " " + lastName)
    email = db.Column("email", db.String(255))
    permission = db.relationship("Permission", backref="user", lazy=True)

class Permission(db.Model):
    __bind_key__ = "users"
    __tablename__ = "permissions"
    id = db.Column("permissionID", db.Integer, primary_key=True)
    level = db.Column("level", db.Integer)
    levelName = db.Column("levelName", db.String(64))
