from flask import Flask, request

app = Flask(__name__)# Put your app in here.

# Calc
# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
# /sub
# Same, subtracting b from a.
# /mult
# Same, multiplying a and b.
# /div
# Same, dividing a by b.
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

@app.route('/add', methods['GET'])
def add(a, b):
    """Add a and b."""
    a = request.args["a"]
    b = request.args["b"]
    
    return a 