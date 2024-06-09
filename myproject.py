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

#create the database class
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
    paternal_state_of_origin = db.Column(db.String(100))
    maternal_state_of_origin = db.Column(db.String(100))
    state_of_residence = db.Column(db.String(100))
    state_of_nysc = db.Column(db.String(100))
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
    future_dream = db.Column(db.String(1000))
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_info')
def new_info():
    return render_template('new_info.html')

@app.route('/post_new_info', methods=["GET", "POST"])
def new_info_post():

    #Assign from HTML to python
    full_name_py = request.form.get('full_name')
    gender_py = request.form.get('gender')
    date_of_birth_py = request.form.get('date_of_birth')
    paternal_state_of_origin_py = request.form.get('paternal_state_of_origin')
    school_py = request.form.get('school')
    level_in_school_py = request.form.get('level_in_school')
    state_of_residence_py = request.form.get('state_of_residence')
    digital_skill_py = request.form.get('digital_skill')
    hubby_py = request.form.get('hubby')
    marital_status_py = request.form.get('marital_status')
    best_food_py = request.form.get('best_food')
    best_friend_py = request.form.get('best_friend')
    nickname_py = request.form.get('nickname')
    religion_py = request.form.get('religion')
    phone_number_py = request.form.get('phone_number')
    maternal_state_of_origin_py = request.form.get('maternal_state_of_origin')
    department_py = request.form.get('department')
    known_from_py = request.form.get('known_from')
    state_of_nysc_py = request.form.get('state_of_nysc')
    non_digital_skill_py = request.form.get('non_digital_skill')
    side_hustle_py = request.form.get('side_hustle')
    future_dream_py = request.form.get('future_dream')
    best_color_py = request.form.get('best_color')
    favorite_place_py = request.form.get('favorite_place')

    #create a new user, that is, to allocate a row to store the information.
    new_user = User(
            full_name = full_name_py,
            gender = gender_py,
            date_of_birth = date_of_birth_py,
            paternal_state_of_origin = paternal_state_of_origin_py,
            school = school_py,
            level_in_school = level_in_school_py,
            state_of_residence = state_of_residence_py,
            digital_skill = digital_skill_py,
            hubby = hubby_py,
            marital_status = marital_status_py,
            best_food = best_food_py,
            best_friend = best_friend_py,
            nickname = nickname_py,
            religion = religion_py,
            phone_number = phone_number_py,
            maternal_state_of_origin = maternal_state_of_origin_py,
            department = department_py,
            known_from = known_from_py,
            state_of_nysc = state_of_nysc_py,
            non_digital_skill = non_digital_skill_py,
            side_hustle = side_hustle_py,
            future_dream = future_dream_py,
            best_color = best_color_py,
            favorite_place = favorite_place_py
            )

    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('main.index'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
