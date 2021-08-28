import re
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return 'We are working on!!!'

@app.route("/id")
def id():
    return render_template('id.html')

@app.route("/elements")
def elements():
    return render_template('elements.html')