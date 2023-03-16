from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)# Put your app in here.


@app.route('/add')
def do_add():
    """call function Add a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """call function turn strings to int to subtract a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """call function turn strings to int to multiply a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    """call function turn strings to int to divide a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    result = div(a, b)
    return str(result)