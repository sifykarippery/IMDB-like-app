from app import db
from sqlalchemy import Sequence


class Profile(db.Model):
    __tablename__ = 'Profiles'

    id = db.Column(db.Integer, Sequence('Profiles_id_seq'), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    dob = db.Column(db.Date())
    address = db.Column(db.String())

    def __init__(self, firstname, lastname, dob, address):
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


class Movie(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, Sequence('Movies_id_seq'), primary_key=True)
    moviename = db.Column(db.String())
    releasedate = db.Column(db.Date())
    budget = db.Column(db.Float())
    collection = db.Column(db.Float())
    description = db.Column(db.Text())

    def __init__(self, moviename, releasedate, budget, collection, description):
        self.moviename = moviename
        self.releasedate = releasedate
        self.budget = budget
        self.collection = collection
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'moviename': self.moviename,
            'releasedate': self.releasedate,
            'budget': self.budget,
            'collection': self.collection,
            'description': self.description
        }


class Actor(db.Model):
    __tablename__ = 'Actors'

    id = db.Column(db.Integer, Sequence('Actors_id_seq'), primary_key=True)
    profileid = db.Column(db.Integer, db.ForeignKey('Profiles.id', ondelete="CASCADE"))
    note = db.Column(db.Text())

    def __init__(self, profileid, note):
        self.profileid = profileid
        self.note = note

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'profileid': self.profileid,
            'note': self.note,
        }


class MovieActor(db.Model):
    __tablename__ = 'MovieActors'

    id = db.Column(db.Integer, Sequence('MovieActors_id_seq'), primary_key=True)
    actorid = db.Column(db.Integer, db.ForeignKey('Actors.id', ondelete="CASCADE"))
    movieid = db.Column(db.Integer, db.ForeignKey('Movies.id', ondelete="CASCADE"))

    def __init__(self, actorid, movieid):
        self.actorid = actorid
        self.movieid = movieid

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'actorid': self.actorid,
            'movieid': self.movieid,
        }


class Director(db.Model):
    __tablename__ = 'Directors'

    id = db.Column(db.Integer, Sequence('Directors_id_seq'), primary_key=True)
    profileid = db.Column(db.Integer, db.ForeignKey('Profiles.id', ondelete="CASCADE"))
    note = db.Column(db.Text())

    def __init__(self, profileid, note):
        self.profileid = profileid
        self.note = note

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'profileid': self.profileid,
            'note': self.note,
        }


class MovieDirector(db.Model):
    __tablename__ = 'MovieDirectors'

    id = db.Column(db.Integer, Sequence('MovieDirectors_id_seq'), primary_key=True)
    directorid = db.Column(db.Integer, db.ForeignKey('Directors.id', ondelete="CASCADE"))
    movieid = db.Column(db.Integer, db.ForeignKey('Movies.id', ondelete="CASCADE"))

    def __init__(self, directorid, movieid):
        self.directorid = directorid
        self.movieid = movieid

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'directorid': self.directorid,
            'movieid': self.movieid,
        }


class Producer(db.Model):
    __tablename__ = 'Producers'

    id = db.Column(db.Integer, Sequence('Producers_id_seq'), primary_key=True)
    profileid = db.Column(db.Integer, db.ForeignKey('Profiles.id', ondelete="CASCADE"))
    note = db.Column(db.Text())

    def __init__(self, profileid, note):
        self.profileid = profileid
        self.note = note

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'profileid': self.profileid,
            'note': self.note,
        }


class MovieProducer(db.Model):
    __tablename__ = 'MovieProducers'

    id = db.Column(db.Integer, Sequence('MovieProducers_id_seq'), primary_key=True)
    producerid = db.Column(db.Integer, db.ForeignKey('Producers.id', ondelete="CASCADE"))
    movieid = db.Column(db.Integer, db.ForeignKey('Movies.id', ondelete="CASCADE"))

    def __init__(self, producerid, movieid):
        self.producerid = producerid
        self.movieid = movieid

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'producerid': self.producerid,
            'movieid': self.movieid,
        }