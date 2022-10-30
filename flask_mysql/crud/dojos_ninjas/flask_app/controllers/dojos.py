from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.dojo import Dojo

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

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('show_ninjas.html', dojo=Dojo.get_one_with_ninjas(data))

# @app.route('/user/destroy/<int:id>')
# def destroy(id):
#     data = {
#         'id':id
#     }
#     User.destroy(data)
#     return redirect('/')

# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data={
#         "id":id #variable id is the actual id number
#     }
#     user=User.get_one(data)
#     return render_template('edit_user.html', user = user)
