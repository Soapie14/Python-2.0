from flask import render_template, redirect, request, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/register', methods=['POST'])
def create_user():
        # if there are errors:
        # We call the staticmethod on Burger model to validate
    valid_user = User.create_valid_user(request.form)
    if not User.validate_user(request.form):
    
        return redirect('/') #redirect to the route where the form is rendered
    session["user_id"] = valid_user.id
    return redirect("/dashboard")
    
    # data ={
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     "email": request.form['email'],
    #     "password": bcrypt.generate_password_hash(request.form['password'])
    # }
    
    # id= User.save(data)
    # session['user_id'] = id
    # return redirect("/dashboard")


@app.route('/login', methods=['POST'])
def login():
    valid_user = User.get_by_email(request.form)
    
    if not valid_user:
        flash("Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(valid_user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = valid_user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("You must be logged in")
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    recipes = Recipe.get_all()
    return render_template("dashboard.html",user=User.get_by_id(data), recipes=recipes)




@app.route("/recipes/edit/<int:recipe_id>")
def recipe_edit_page(recipe_id):
    recipe = Recipe.get_by_id(recipe_id)
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/recipes/delete/<int:recipe_id>")
def delete_by_id(recipe_id):
    Recipe.delete_recipe_by_id(recipe_id)
    return redirect("/recipes/home")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')