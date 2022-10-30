from flask import render_template, redirect, request

from flask_app import app
from flask_app.models import ninja, dojo



@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos=dojo.Dojo.get_all())

@app.route('/process', methods=['POST'])
def new_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
