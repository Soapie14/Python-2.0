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
    valid_recipe = Recipe.create_valid_recipe(request.form)
    if valid_recipe:
        return redirect(f'/recipes/{valid_recipe.id}')
    return redirect('/recipe/new')

@app.route("/recipes/<int:recipe.id>")
def recipe_detail(recipe_id):
    user = User.get_by_id(session["user_id"])
    recipe = Recipe.get_by_id(recipe_id)
    return render_template("view_recipe.html", user=user, recipe=recipe)

@app.route("/recipes/<int:recipe_id>", methods=["POST"])
def update_recipe(recipe_id):

    valid_recipe = Recipe.update_recipe(request.form, session["user_id"])

    if not valid_recipe:
        return redirect(f"/recipes/edit/{recipe_id}")
        
    return redirect(f"/recipes/{recipe_id}")