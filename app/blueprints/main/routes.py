from .import bp as main
from flask import current_app as app, render_template

#route for homepage
@main.route('/')
def index():
    return render_template('index.html')
    
#route for attorneys
@main.route('/attorneys')
def attorneys():
    return render_template('attorneys.html')

#route for whatwedo
@main.route('/whatwedo')
def whatwedo():
    return render_template("whatwedo.html")

#route for whoweare
@main.route('/whoweare')
def whoweare():
    return render_template("whoweare.html")

#route for wherewework
@main.route('/wherewework')
def wherewework():
    return render_template("wherewework.html")

#route for contactus
@main.route('/contactus')
def contactus():
    return render_template("contactus.html")


