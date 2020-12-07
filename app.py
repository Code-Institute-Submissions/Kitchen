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
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


# sign in --------------------------------------------------------------------
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
                    flash("Hi there, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if password doesn't match
                flash("The Username and/or Password is incorrect!")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("The Username doesn't exist! Please try again.")
            return redirect(url_for("signin"))

    return render_template("signin.html")


# users profile ---------------------------------------------------------
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # session username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("signin"))


# log out ----------------------------------------------------------------
@app.route("/logout")
def logout():
    # log out by deleting session cookies
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("signin"))


# add recipe -------------------------------------------------------------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_name": request.form.get("recipe_name"),
            "preptime_time": request.form.get("preptime_time"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation_steps": request.form.getlist("preparation_steps"),
            "created_by": session["user"]
        }
        mongo.db.recipies.insert_one(recipe)
        flash("Recipe Added!")
        return redirect(url_for("get_recipies"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    preptimes = mongo.db.preptime.find().sort("preptime_time", 1)
    return render_template(
        "add_recipe.html", categories=categories, preptime=preptimes)


# edit recipe -------------------------------------------------------------
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    preptimes = mongo.db.preptime.find().sort("preptime_time", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories, preptime=preptimes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
