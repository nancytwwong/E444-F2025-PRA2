#Example 2-1. hello.py: A complete Flask application
#Example 2-2. hello.py: Flask application with a dynamic route
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return '<h1>Hello World!</h1>'

#@app.route('/user/<name>')
#def user(name):
#    return '<h1>Hello, {}!</h1>'.format(name)

#if __name__ == '__main__':
#    app.run()

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

def validEmail(form, field):
    if "@" not in field.data:
        raise ValidationError("Please include an '@' in the email address. %s is missing an '@'." %(field.data))


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField("What is your UofT Email address?", validators=[DataRequired(), validEmail])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = NameForm() 
    if form.validate_on_submit(): 
        old_name = session.get('name') 
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data: 
            flash('Looks like you have changed your name!') 

        if old_email is not None and old_email != form.email.data: 
            flash('Looks like you have changed your email!') 

        session['name'] = form.name.data 
        session['email'] = form.email.data 
        return redirect(url_for('index')) 
    return render_template('index.html', current_time=datetime.utcnow(), form = form, name = session.get('name'), email = session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)