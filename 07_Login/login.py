import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from flask import render_template, redirect, request, url_for, flash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

from flask_bootstrap import Bootstrap

from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')

# make sure app secret exists
# generate i.e. via openssl rand -base64 32
assert 'APP_SECRET' in os.environ, 'need to set APP_SECRET environ variable.'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/cs6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:docker@localhost/postgres'
app.config['SECRET_KEY'] = os.environ['APP_SECRET']
db = SQLAlchemy(app)

Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' # route or function where login occurs...

# create model
class User(UserMixin, db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is write-only')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route('/')
@login_required
def index():

    return 'Hello world'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)

            return redirect(url_for('secret_page'))
        flash('invalid username or password.')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/secret')
@login_required
def secret_page():
    return 'This is the secret of this application'

if __name__ == '__main__':
    app.run(debug=True)
