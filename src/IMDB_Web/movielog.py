from app import db
from sqlalchemy import Sequence



class MovieLog(db.Model):
    __tablename__ = 'movielogs'

    id = db.Column(db.Integer, Sequence('movielogs_id_seq'), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    dob = db.Column(db.Date())
    address = db.Column(db.String())

    def __init__(self, id, firstname, lastname, dob, address):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.address = address

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'dob': self.dob,
            'address': self.address
        }