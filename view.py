from app import app
from flask import render_template, flash
from models import User,db
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template,redirect, url_for,request
from werkzeug.security import generate_password_hash, check_password_hash
from places import  _places_uzb, UZB

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return 'We are working on!!!'

@app.route("/main")
def main():
    if current_user.is_authenticated:
        return render_template('main.html',name=current_user.name)
    else:
        return redirect(url_for('login'))




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
            flash('Yana bir bor akkount tekshiring')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('main'))

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
            flash('Bu email adress mavjud')
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
    return redirect(url_for('index'))

@app.route("/main/uzb/<id>", methods=['GET', 'POST'])
def main_uzb(id):
    if int(id) < len(UZB):
        if current_user.is_authenticated:
            if request.method == 'GET':
                return render_template('id.html',name=current_user.name,  locate=UZB[int(id)], list_four=_places_uzb(int(id)),id=id)
            elif request.method == 'POST':
                result = request.form.get('result')
                client_res = UZB[int(id)][0].split(' ')
                if client_res[0] == result:
                    return redirect(f'/main/uzb/{int(id) + 1}')
                flash('Noto\'g\'ri javob')
                return redirect(f'/main/uzb/{id}')
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('main'))


@app.route("/main/usa")
def main_usa():
    if current_user.is_authenticated:
        return 'Under development...'
    else:
        return redirect('auth/login')

@app.route("/main/global")
def main_global():
    if current_user.is_authenticated:
        return 'Under development...'
    else:
        return redirect('auth/login')
@app.errorhandler(404) 
def page_not_found(e):
    return redirect(url_for('index'))
# db.create_all()

    