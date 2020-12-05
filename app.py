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
# get home page --------------------------------------------------------------
@app.route("/get_home")
def get_home():
    home = mongo.db.home.find()
    return render_template("index.html", home=home)


# get recipies page ---------------------------------------------------------
@app.route("/get_recipies")
def get_recipies():
    recipies = mongo.db.recipies.find()
    return render_template("recipies.html", recipies=recipies)


# get signup page ---------------------------------------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Checking if username exist
        user_existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_existing:
            flash("Username already exists!")
            return redirect(url_for("signup"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # session cookie for new user
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if user exists
        user_existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_existing:
            # check password match
            if check_password_hash(
                user_existing["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hi there, {}!".format(request.form.get("username")))
            else:
                # if password doesn't match
                flash("The Username and/or Password is incorrect!")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("The Username doesn't exist! Please try again.")
            return redirect(url_for("signin"))

    return render_template("signin.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
