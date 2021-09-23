import sqlite3
from db import db
#model is our internal representation of an entity
#The User class is a helper that is used to store data about the user and allow us to easily retrieve user object from a database. 
#This is an API. The methods here are an interface for other parts of the our program to interact with user thing. Which includes writing user to database and retrieving it. 

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password 

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
