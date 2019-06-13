import os

from flask import Flask, request, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/add")
# def add_profile():
#     firstname=request.args.get('firstname')
#     lastname=request.args.get('lastname')
#     dob=request.args.get('dob')
#     address=request.args.get('address')
#     try:
#         profile=Profile(
#             firstname=firstname,
#             lastname=lastname,
#             dob=dob,
#             address=address
#         )
#         db.session.add(profile)
#         db.session.commit()
#         return "Profile added. profile id={}".format(profile.id)
#     except Exception as e:
# 	    return(str(e))
#
# @app.route("/getall")
# def get_all():
#     try:
#         profiles=Profile.query.all()
#         return  jsonify([e.serialize() for e in profiles])
#     except Exception as e:
# 	    return(str(e))
#
# @app.route("/get/<id_>")
# def get_by_id(id_):
#     try:
#         profile=Profile.query.filter_by(id=id_).first()
#         return jsonify(profile.serialize())
#     except Exception as e:
# 	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_profile_form():
    if request.method == 'POST':
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        dob=request.form.get('dob')
        address=request.form.get('address')
        try:
            profile= Profile(
                firstname=firstname,
                lastname=lastname,
                dob=dob,
                address=address
            )
            db.session.add(profile)
            db.session.commit()
            return "profile added. Profile id={}".format(profile.id)
        except Exception as e:
            return(str(e))
    return render_template("profiledata.html")


@app.route("/movies",methods=['POST'])
def add_movie():

    print(request.is_json)
    payload = request.get_json()
    producer_profile=[]
    actor_profiles=[]
    director_profiles = []
    n=payload["producers"]
    m=payload["actors"]
    l=payload["directors"]
    for i in n:
        profile = Profile(
            firstname=i["firstname"],
            lastname=i["lastname"],
            dob=i["dob"],
            address=i["description"]
        )

        db.session.add(profile)
        db.session.commit()

        producer=Producer(
            profileid=profile.id,
            note="note"
        )
        db.session.add(producer)
        db.session.commit()
        producer_profile.append(producer.id)

    for i in m:
        actor_profile=Profile(
            firstname=i["firstname"],
            lastname=i["lastname"],
            dob=i["dob"],
            address=i["description"]
        )
        db.session.add(actor_profile)
        db.session.commit()

        actor=Actor(
            profileid=actor_profile.id,
            note="note"
        )
        db.session.add(producer)
        db.session.commit()
        actor_profiles.append(actor.id)

    for i in l:
        director_profile = Profile(
            firstname=i["firstname"],
            lastname=i["lastname"],
            dob=i["dob"],
            address=i["description"]
            )
        db.session.add(director_profile)
        db.session.commit()
        director = Director(
                profileid=actor_profile.id,
                note="note"
            )
        db.session.add(director)
        db.session.commit()
        director_profiles.append(director.id)

    newmovie=Movie(moviename=payload["moviename"],
                   releasedate=payload["releasedate"],
                   collection=payload["collection"],
                   budget=0.0,
                   description=payload["description"])
    db.session.add(newmovie)
    db.session.commit()

    for i in producer_profile:
        producer_movie=MovieProducer(
            producerid=i,
            movieid=newmovie.id
        )
        db.session.add(producer_movie)
        db.session.commit()

    for i in actor_profiles:
        actor_movie = MovieActor(
            actorid=i,
            movieid=newmovie.id
            )
        db.session.add(actor_movie)
        db.session.commit()

    for i in director_profiles:
        director_movie = MovieDirector(
            directorid=i,
            movieid=newmovie.id
            )
        db.session.add(director_movie)
        db.session.commit()

    print(newmovie)
    return jsonify(newmovie.serialize())

if __name__ == '__main__':
    app.run()