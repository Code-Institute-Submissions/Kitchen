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
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("index.html", home=home, categories=categories)


# get recipies page ---------------------------------------------------------
@app.route("/get_recipies")
def get_recipies():
    recipies = mongo.db.recipies.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "recipies.html", recipies=recipies, categories=categories)


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
    # for users recipies
    recipies = mongo.db.recipies.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipies=recipies)

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
            "ingredients": request.form.get("ingredients"),
            "preparation_steps": request.form.get("preparation_steps"),
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
    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_name": request.form.get("recipe_name"),
            "preptime_time": request.form.get("preptime_time"),
            "ingredients": request.form.get("ingredients"),
            "preparation_steps": request.form.get(
                "preparation_steps"),
            "created_by": session["user"]
        }
        mongo.db.recipies.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Edited!")

    recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    preptimes = mongo.db.preptime.find().sort("preptime_time", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories, preptime=preptimes)


# delete recipe -------------------------------------------------------------
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted!")
    return redirect(url_for('get_recipies'))


# categories -------------------------------------------------------------
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add categories ----------------------------------------------------------
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "recipe_img": request.form.get("recipe_img")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit categories ----------------------------------------------------------
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_img": request.form.get("recipe_img")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete categories ----------------------------------------------------------
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("get_categories"))


# select recipe ----------------------------------------------------------
@app.route("/select_recipe/<recipe_id>")
def select_recipe(recipe_id):
    selected_recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "select_recipe.html", recipe=selected_recipe)


# select category ----------------------------------------------------------
@app.route("/select_category/<category_id>")
def select_category(category_id):
    # for selecting a new category from category section
    categories = mongo.db.categories.find().sort("category_name", 1)
    # connecting to the category id
    selected_category = mongo.db.categories.find_one({
        "_id": ObjectId(category_id)
        })
    # selected category recipies
    recipies = mongo.db.recipies.find()
    return render_template(
        "select_category.html", category=selected_category,
        recipies=recipies, categories=categories)


# 404 error ----------------------------------------------------------
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    # returns the 404.html page
    return render_template('404.html'), 404


# 500 error ----------------------------------------------------------
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(500)
def internal_server_error(e):
    # returns the 500.html page
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
