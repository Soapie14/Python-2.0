from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def index():
    
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count']+=1
    
    return render_template("index.html", count=session['count'])

@app.route("/count", methods=["POST"])
def show_count():
    
    if request.form["more"] =="reset":
        session.clear()
    elif request.form["more"] == "add_2":
        session['count'] +=1
    return redirect("/")

    
# @app.route("/destroy")
# def destroy():
#     session.clear()
#     return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)