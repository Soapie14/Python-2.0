from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/theform')
def form():
    return render_template("form.html")

@app.route('/form', methods=['post'])
def formpost():
    print(f"Post Route: {request.form}")
    return render_template("form.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'NOPE, TRY AGAIN'
if __name__ == "__main__":
    app.run(debug=True)