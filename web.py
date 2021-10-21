from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import render_template
from flask import request
import smtplib

from flask_wtf import form
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET KEY'] = '76538617b77f1104fdfa4bdcfa522fec'

# initialize database
db = SQLAlchemy(app)

# create db model
class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Func to return string
    def __repr__(self):
        return '<Name %r' % self.id


# posts = [
#     {
#         'user': 'Redwan Doe',
#         'title': 'First Post',
#         'content': 'Lorem ipsum pls',
#         'date_posted': '10-13-2021 11:27 PM'
#     },
#     {
#         'user': 'Jane Doe',
#         'title': 'Second Post',
#         'content': 'Lorem ipsum pls stop',
#         'date_posted': '10-13-2021 11:29 PM'
#     }
# ]

members = []

@app.route("/")
def home():
    return render_template('home.html')
   

@app.route("/contacts", methods=["POST"])
def contacts():

# ADD EMAIL AND PASS IF YOU WANT THIS TO WORK
    # msg = 'Welcome! we cover news out of this world'
    # server = smtplib.SMTP("stmp.gmail.com", 587)
    # server.starttls()
    # server.login("virus.run.py@gmail.com")
    # server.sendmail("virus.run.py@gmail.com", msg)



    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone_number = request.form.get("phone_number")
    
    if not first_name or not last_name or not phone_number:
        error_statement = "Fill Required Fields"
        return render_template('home.html', error_statement=error_statement, first_name=first_name,
        last_name=last_name, 
        phone_number=phone_number)

    members.append(f" {first_name} {last_name} {phone_number} ")

    title = 'Thank you!'
    return render_template('info.html', members=members, title=title, first_name=first_name,
    last_name=last_name, 
    phone_number=phone_number)

@app.route("/ring")
def ring():
   return render_template('ring.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)



if __name__ == '__main__':
    app.run(debug=True)