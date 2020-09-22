from .import bp as authentication
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from .forms import FullForm, LoginForm
from .models import User

# route for register using a WTForm
@authentication.route('/register', methods=['GET', 'POST'])
def register():
    # set an instance of the form
    form = FullForm()
    
    if form.validate_on_submit():
        # collect the data from the form into a dictionary
        data = {
            'first_name' : request.form.get('first_name'),
            'last_name' : request.form.get('last_name'),
            'email' : request.form.get('email'),
            'password' : request.form.get('password')
        }
        # create an instance of the User class using the data dictionary
        u = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
        # securing the password
        u.hash_pass(u.password)
        # adding the user to the database
        db.session.add(u)
        db.session.commit()
        # confirmations
        flash("You have succesfully registered!", 'primary')
        # send them to a login page
        return redirect(url_for("authentication.login"))
    content = {
        'form': form
    }
    return render_template('register.html', **content)

# route for login using a WTform
@authentication.route('/login', methods=['GET', 'POST'])
def login():
    # set an instance of the form
    form = LoginForm()

    user = User.query.filter_by(email=request.form.get('email')).first()
    if form.validate_on_submit():
        # check if the info is correct
        if user is None or not user.check_password(request.form.get('password')):
            flash("You have entered incorrect details, please try again", 'danger')
            return redirect(url_for('login'))
        login_user(user)
        flash("You have successfully logged in!", 'success')
        return redirect(url_for('main.index'))
    content = {
        'form' : form
    }
    return render_template('login.html', **content)

# logout route, pretty simple
@authentication.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out!", 'info')
    return redirect(url_for("authentication.login"))

