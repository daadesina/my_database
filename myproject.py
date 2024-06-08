#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, url_for, request, redirect

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secrete_key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

main = Blueprint('main', __name__)
main_blueprint = main
app.register_blueprint(main_blueprint)

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=True)
    nickname = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    department = db.Column(db.String(100))
    school = db.Column(db.String(100))
    level_in_school = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))
    state_of_origin = db.Column(db.String(100))
    state_of_residence = db.Column(db.String(100))
    religion = db.Column(db.String(100))
    marital_status = db.Column(db.String(100))
    known_from = db.Column(db.String(100))
    digital_skill = db.Column(db.String(100))
    non_digital_skill = db.Column(db.String(100))
    side_hustle = db.Column(db.String(100))
    best_food = db.Column(db.String(100))
    best_color = db.Column(db.String(100))
    best_friend = db.Column(db.String(100))
    favorite_place = db.Column(db.String(100))
    hubby = db.Column(db.String(100))
    dream = db.Column(db.String(1000))
    

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
