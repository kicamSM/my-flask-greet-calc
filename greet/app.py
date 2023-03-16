from flask import Flask, request

app = Flask(__name__)
# Greet
# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”
# Once you’ve finished this, run the tests for it:

# python3 -m unittest test.py


@app.route('/welcome')
def welcome():
    return "welcome" 

@app.route('/welcome/home')
def welcome_home():
    return "welcome home" 

@app.route('/welcome/back')
def welcome_back():
    return "welcome back" 

