from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos=Dojo.get_all())

@app.route('/process', methods=['POST'])
def new_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/ninja/destroy/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    Ninja.destroy(data)
    return redirect('/')

@app.route('/ninja/edit', methods=['POST'])
def update():
    Ninja.update(request.form)
    return redirect('/')

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data={
        "id":id #variable id is the actual id number
    }
    ninja=Ninja.get_one(data)
    return render_template('edit_ninja.html', ninja = ninja)