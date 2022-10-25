from types import BuiltinFunctionType
from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def root():
    return 'Root Route'

@app.route('/play')
def box1():
    return render_template('index.html', num=3, color = 'blue')

@app.route('/play/<int:num>')
def moreboxes(num):
    return render_template('index.html', num=num, color = 'blue')

@app.route('/play/<int:num>/<color>')
def boxcolor(num, color):
    return render_template('index.html', num=num, color=color)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return 'NOPE, TRY AGAIN'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
