from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/recipe/new")
def recipe_create_page():
    return render_template("new_recipe.html")

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    valid_recipe = Recipe.create_valid_recipe(request.form)
    if valid_recipe:
        return redirect(f'/recipe/{valid_recipe.id}')
    return redirect('/recipe/new/')



@app.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    user = User.get_by_id(session["user_id"])
    recipe = Recipe.get_by_id(recipe_id)
    return render_template("view_recipe.html", user=user, recipe=recipe)



@app.route("/recipe_edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    recipe = Recipe.get_by_id(recipe_id)
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/recipe/<int:recipe_id>", methods=["POST"])
def update_recipe(recipe_id):

    valid_recipe = Recipe.update_recipe(request.form, session["user_id"])

    if not valid_recipe:
        return redirect(f"/recipe_edit/{recipe_id}")
        
    return redirect(f"/recipe/{recipe_id}")

@app.route("/recipe/delete/<int:recipe_id>")
def delete_by_id(recipe_id):
    Recipe.delete_recipe_by_id(recipe_id)
    return redirect("/dashboard")