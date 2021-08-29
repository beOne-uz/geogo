from app import app
from flask import render_template, flash
from models import User,db
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template,redirect, url_for,request
from werkzeug.security import generate_password_hash, check_password_hash


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
    if current_user.is_authenticated:
        return render_template('id.html',name=current_user.name)
    else: 
        return render_template('id.html',name='Guest')

@app.route("/elements")
def elements():
    return render_template('elements.html')

@app.route('/auth/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signin.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True 

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('index'))

@app.route('/auth/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        last_name = request.form.get('last_name')

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect('signup')

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email,last_name=last_name, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('id'))

# @app.route('/auth/signup',methods=['POST'])
# def signup_post():
    

# db.create_all()

    