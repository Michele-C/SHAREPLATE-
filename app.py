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
                flash("Welcome {}".format(request.form.get("username")))
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

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # This function removes users cookies.
    flash("You have logged out see you soon again.")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_recipes")
def add_recipes():
    categories=mongo.db.categories.find().sort("category_name", 1)
    stars=mongo.db.stars.find().sort("star_rating", 1) 
    return render_template("add_recipes.html", categories=categories, stars=stars)     

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
