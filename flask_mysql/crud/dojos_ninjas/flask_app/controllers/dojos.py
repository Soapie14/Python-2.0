from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', all_dojos = dojos)

@app.route('/new/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>') #integer value with name of ID
def show_dojo(id): #ID is grabbed from our route
    data = {
        "id": id 
    }
    return render_template('show_ninjas.html', dojo=Dojo.get_one_with_ninjas(data))


