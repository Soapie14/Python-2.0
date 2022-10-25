from flask_app import app #importing flask app 
from flask_app.controllers import items_controller #items_controller is an example for importing our folder from controllers

if __name__ == "__main__": #always need to debug
    app.run(debug=True)
    