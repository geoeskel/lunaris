import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find())
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("library", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches the one typed by the user
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "library", username=session["user"]))
            else:
                # incorrect password
                flash("The username and/or password you provided are not correct. Pleast try again.")
                return redirect(url_for("login"))

        else:
            # incorrect user
            flash("The username and/or password you provided are not correct. Pleast try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/library/<username>", methods=["GET", "POST"])
def library(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("library.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Delete user's cookies from the session 
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_movie")
def add_movie():
    genre = mongo.db.genre.find().sort("genre_name", 1)
    source_name = mongo.db.available_on.find().sort("source_name", 1)
    rating_value = mongo.db.ratings.find().sort("rating_value", 1)
    return render_template(
        "add_movie.html", genre=genre, source_name=source_name, rating_value=rating_value)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
