from app import db
from sqlalchemy import Sequence

class Profile(db.Model):
    __tablename__ = 'Profiles'

    id = db.Column(db.Integer, Sequence('profiles_id_seq'), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    dob = db.Column(db.Date())
    address=db.Column(db.String())

    def __init__(self, id, firstname, lastname,dob,address):
        self.id = id
        self.firstname = firstname
        self.lastname= lastname
        self.dob=dob
        self.address=address

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'dob': self.dob,
            'address':self.address
        }


class Movie(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, Sequence('movies_id_seq'), primary_key=True)
    moviename = db.Column(db.String())
    releasedate = db.Column(db.Date())
    budget=db.Column(db.Float())
    collection=db.Column(db.Float())
    description=db.Column(db.Text())

    def __init__(self, id, moviename, releasedate, budget, collection, description):
        self.id = id
        self.moviename = moviename
        self.releasedate= releasedate
        self.budget=budget
        self.collection=collection
        self.description=description

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'moviename': self.moviename,
            'releasedate': self.releasedate,
            'budget': self.budget,
            'collection':self.collection,
            'self.description':self.description
        }


