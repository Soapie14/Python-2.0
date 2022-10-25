from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets are no fun' 

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['fave_lang'] = request.form['fave_lang']
    session['comments'] = request.form['comments']
    # blah= request.form.get("hello") # Example of if statement as a request form, if hello exists, display it
    return redirect('/results')

@app.route('/results')
def show_responses():
    return render_template('show.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True) 