import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ["IMDB_APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Profile, Movie


@app.route("/")
def healthcheck():
    return "Site is healthy!"


@app.route("/movie/<name>")
def get_movie_name(name):
    return "Movie : {}".format(name)


@app.route("/details")
def get_movie_details():
    movie = request.args.get('movie')
    return "Author : {}".format(movie)


if __name__ == '__main__':
    app.run()