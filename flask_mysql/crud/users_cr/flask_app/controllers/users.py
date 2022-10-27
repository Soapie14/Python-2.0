from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def root():
    return redirect('/users')

@app.route('/users')
def results():
    return render_template("show.html", users=User.get_all())

@app.route('/users/new')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def userForm():
    User.save(request.form)
    return redirect('/users')