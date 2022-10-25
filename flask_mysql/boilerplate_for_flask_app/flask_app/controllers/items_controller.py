from flask_app import app
from flask import redirect, render_template, request #we need request for passing in our request form
from flask_app.models.items import Item #importing our class of items (each item) through our model 

@app.route('/')
def index():
    return render_template("items.html", items=Item.get_all) # can add in data from our model, this also gives us access in our html


@app.route('/new/item')
def new_item_form():
    return render_template("new_item.html")

@app.route('/create/item', method='POST')
def add_item():
    Item.save(request.form)
    return redirect('/')