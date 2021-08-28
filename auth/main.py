from flask import Blueprint
from flask import render_template,redirect, url_for,request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User,db
auth = Blueprint('auth', __name__)




@auth.route('/login')
def login():
    return render_template('signin.html')

@auth.route('/signup',methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'