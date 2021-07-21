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
def home():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in our db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Dictionary to accept values to allow input into db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have Registered Successfully!")
        # redirects you to the profile page
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# login view
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Coping Tims CI code for this login tests
        # check in case username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # we are making sure that hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username").capitalize()))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect Username and / or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist but throwing a password problem in there
            flash("Incorrect Username and / or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # take the session user username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find())    

    if session["user"]:
        return render_template("profile.html", username=username, recipes=recipes)
    
    return redirect(url_for("/home"))


@app.route("/logout")
def logout():
    # This function removes users session cookies.
    flash("You have logged out see you soon again.")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "star_rating": request.form.get("star_rating"),
            "cuisine": request.form.get("cuisine"),
            "tools": request.form.get("tools"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
    categories=mongo.db.categories.find().sort("category_name", 1)
    stars=mongo.db.stars.find().sort("star_rating", 1) 
    return render_template(
        "add_recipes.html", categories=categories, stars=stars) 


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
# the post method

    if request.method == "POST":
        updated_recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "star_rating": request.form.get("star_rating"),
            "cuisine": request.form.get("cuisine"),
            "tools": request.form.get("tools"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        # First parameter says which recipe to up date , second is updated data
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, updated_recipe)
        flash("Recipe Successfully Updated")

    # defining variables 
    recipe = mongo.db.recipes.find_one({"_id" : ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    stars = mongo.db.stars.find().sort("star_rating", 1) 
    # the get method
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories, stars=stars)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Removed")
    return redirect(url_for("recipes"))


@app.route("/list_category") 
def list_category():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        #  Dictionary to be inserted into db
        category = {
            "category_name": request.form.get("category_name")
        }
        # db collection that we are putting our variable into
        mongo.db.categories.insert_one(category)
        flash("Successfully Added Category")
        return redirect(url_for("list_category"))

    # get method
    return render_template("add_category.html")

@app.route("/edit_category/<category_id>", methods= ["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        update_category = {
            "category_name": request.form.get("category_name")
        }
    # update takes 2 dictionaries 1st: which specific category to update and 2nd: the new info    
        mongo.db.categories.update({"_id": ObjectId(category_id)}, update_category)
        flash("Successfully Updated Category")
        return redirect(url_for("list_category"))
    # Get method
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>") 
def delete_category(category_id):
    category = mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Successfully Removed Category") 
    return redirect(url_for("list_category"))




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
