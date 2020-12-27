"""Kitchen - Milestone 3 Project.

This project was made with guidance from the
Mini Project - Task Manager | Putting It All Together led by Tim

(c) by Josefine Kihlström 2020.
"""

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
@app.route("/get_home")
def get_home():
    """Takes the user to the home page.

    Categories variable finds and displays the categories stored in the MongoDB
    database. The value then sorts the categories alphabetically.

    Returns the index.html page.
    """

    home = mongo.db.home.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("index.html", home=home, categories=categories)


@app.route("/get_recipies")
def get_recipies():
    """Takes the user to the recipes page.

    Recipies variable finds and displays the recipies stored in the MongoDB
    database and categories variable finds and displays the categories stored
    in the MongoDB database with a value that sorts the categories
    alphabetically.

    Returns the recipies.html page.
    """

    recipies = list(mongo.db.recipies.find())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "recipies.html", recipies=recipies, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Search function.

    Query variable connects to the MongoDB text index. The function
    searches the text within the recipe ingredients and recipe name.
    Recipies variable finds and displays the recipies stored in the MongoDB
    database containing the keywords used in the search function.
    Categories variable finds and displays all the categories
    stored in the MongoDB database.

    Returns the recipies.html page.
    """

    query = request.form.get("query")
    recipies = list(mongo.db.recipies.find({"$text": {"$search": query}}))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "recipies.html", recipies=recipies, categories=categories)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Allows the user to sign up to the page.

    The user_existing variable checks if the username is already existing.
    If the username already exists, the page will redirect to the signup.html
    page with a flash message displaying.
    The register variable registers the username and password in
    the MongoDB database. The password is encrypted before sent to
    the database.
    When new user is signed up the page redirects to the profile page
    displaying a flash message.

    Returns the signup.html page
    """

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


@app.route("/signin", methods=["GET", "POST"])
def signin():
    """Allows the user to sign in to the page.

    The user_existing variable checks if the user exists in the database.
    If the user exist and password is correct the user is redirected to the
    profile page with a flash message displaying.
    If the password doesn't match the user is redirected to the signin.html
    page with a flash message displaying.
    If the username doesn't exist, the user is redirected to the signin.page
    with a flash message displaying.

    Returns the signin.html page.
    """

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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Takes the user to the profile page

    Username variable checks the session username and returns
    the users profile page.
    Recipies variable finds and displays the recipes from the database.

    Returns the signin page if no session user.
    """
    # session username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # for users recipes
    recipies = mongo.db.recipies.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipies=recipies)

    return redirect(url_for("signin"))


@app.route("/logout")
def logout():
    """Function that removes session cookie and logs user out.
    Returns the signin.html page with a flash message displaying.
    """

    flash("You have logged out")
    # log out by deleting session cookies
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """Function to add new user recipe.

    Recipe variable takes the recipe keys and values that gets sent
    to the MongoDB and returns the recipies.html page with a flash message
    displaying.
    Categories variable gets the category values from the database to option
    list for categories and preptimes gets the preptime values from
    the database to the option list for preptimes.

    Returns the add_recipe.html page.
    """

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


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """Function to edit recipes from the database.

    Edit variable takes the edited recipe keys and values that gets sent
    to the MongoDB and returns the edit_recipies.html page with a flash
    message displaying.
    The recipe variable finds the recipe id that is to be edited.
    Categories variable gets the category values from the database to the
    option list for categories and preptimes gets the preptime values from
    the database to the option list for preptimes.

    Returns the edit_recipe.html page.
    """
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


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Function to delete a recipe by its id.
    Returns the recipies.html page with a flash message displaying.
    """

    mongo.db.recipies.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted!")
    return redirect(url_for('get_recipies'))


@app.route("/get_categories")
def get_categories():
    """Function that displays categories.
    Returns the categories.html page.
    """

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """Function to add new category.

    The category variable takes the category key and values that gets sent
    to the MongoDB database.
    When a new category is added the user redirected to the categories.html
    page with a flash message displaying.

    Returns the add_category.html page.
    """

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "recipe_img": request.form.get("recipe_img")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """Function to edit category.

    The submit variable takes the edited category key and values that gets sent
    to the MongoDB database.
    The Admin user is the only one who can edit a category.
    When a category is edited the admin user is redirected to the
    categories.html page with a flash message displaying.
    The category variable gets the category id that is to be edited.

    Returns the edit_category.html page.
    """

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


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """Function that deletes a category by its id.
    Returns the categories.html page with a flash message displaying.
    """

    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("get_categories"))


@app.route("/select_recipe/<recipe_id>")
def select_recipe(recipe_id):
    """Function that shows selected recipe.

    The selected_recipe variable finds the recipe id and returns the
    select_recipe.html page.
    """

    selected_recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "select_recipe.html", recipe=selected_recipe)


@app.route("/select_category/<category_id>")
def select_category(category_id):
    """Function that shows selected category recipes.

    The categories variable finds all the categories from the database
    that will be displaying on the page for the user to pick a new category.
    The selected_category variable finds the selected category id.
    The recipies variable finds the recipies from the database that will be
    displaying on the page.

    Returns the select_category.html page.
    """
    # for selecting a new category from category section
    categories = mongo.db.categories.find().sort("category_name", 1)
    # connecting to the category id
    selected_category = mongo.db.categories.find_one({
        "_id": ObjectId(category_id)
        })
    # selected category recipes
    recipies = mongo.db.recipies.find()
    return render_template(
        "select_category.html", category=selected_category,
        recipies=recipies, categories=categories)


@app.errorhandler(404)
def page_not_found(e):
    """If page is not found.

    Code with help from:
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/

    Returns the 404.html page.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """If internal server error.

    Code with help from:
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/

    Returns the 500.html page.
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
