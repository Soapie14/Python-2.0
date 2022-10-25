from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'Root Route'

@app.route('/home')
def dashboard():
    return 'Houston we have a problem.'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return 'NOPE, TRY AGAIN'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
