from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy import * 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/Users/utuckn1/ISEAGE/vulnerable-flask/app/vulnerable.db'

db = sqlalchemy(app)

class User(db.Model):
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    if request.method == 'POST':
        return 'cdc{good_request}'
    else:
        return 'change your methods'