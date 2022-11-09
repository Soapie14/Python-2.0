from flask import render_template, redirect, request, session, flash

from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/recipe/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/create_recipe', methods=['POST'])
def create():
    Recipe.save(request.form)
    return redirect('/dashboard')