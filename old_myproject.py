#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, url_for, request, redirect
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine




basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secrete_key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')

db = SQLAlchemy(app)

#with app.app_context():
#        db.create_all()

main = Blueprint('main', __name__)
main_blueprint = main
app.register_blueprint(main_blueprint)

#create the database table
class Member(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=True)
    nickname = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    religion = db.Column(db.String(100))
    month_of_birth = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))
    department = db.Column(db.String(100))
    school = db.Column(db.String(100))
    level_in_school = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(100))
    paternal_state_of_origin = db.Column(db.String(100))
    maternal_state_of_origin = db.Column(db.String(100))
    state_of_residence = db.Column(db.String(100))
    state_of_nysc = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
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

@app.route('/new_info_post', methods=["GET", "POST"])
def new_info_post():

    #Assign from HTML to python
    full_name_py = request.form.get('full_name_html')
    gender_py = request.form.get('gender_html')
    month_of_birth_py = request.form.get('month_of_birth_html')
    date_of_birth_py = request.form.get('date_of_birth_html')
    paternal_state_of_origin_py = request.form.get('paternal_state_of_origin_html')
    school_py = request.form.get('school_html')
    level_in_school_py = request.form.get('level_in_school_html')
    state_of_residence_py = request.form.get('state_of_residence_html')
    digital_skill_py = request.form.get('digital_skill_html')
    hubby_py = request.form.get('hubby_html')
    marital_status_py = request.form.get('marital_status_html')
    best_food_py = request.form.get('best_food_html')
    best_friend_py = request.form.get('best_friend_html')
    nickname_py = request.form.get('nickname_html')
    religion_py = request.form.get('religion_html')
    phone_number_py = request.form.get('phone_number_html')
    maternal_state_of_origin_py = request.form.get('maternal_state_of_origin_html')
    department_py = request.form.get('department_html')
    known_from_py = request.form.get('known_from_html')
    state_of_nysc_py = request.form.get('state_of_nysc_html')
    non_digital_skill_py = request.form.get('non_digital_skill_html')
    side_hustle_py = request.form.get('side_hustle_html')
    future_dream_py = request.form.get('future_dream_html')
    best_color_py = request.form.get('best_color_html')
    favorite_place_py = request.form.get('favorite_place_html')

    #create a new user, that is, to allocate a row to store the information.

    print (f"My name is: {full_name_py}")

    new_user = Member(
            full_name = full_name_py,
            gender = gender_py,
            month_of_birth = month_of_birth_py,
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


    return redirect(url_for('index'))

@app.route('/show_data')
def show_data():
    return render_template('show_data.html')

@app.route('/pre_show_data')
def pre_show_data():
    engine = create_engine('sqlite:///db.sqlite')
    query = """SELECT * FROM member;"""
    df = pd.read_sql(query, engine)
    #df = pd.read_sql_table('member', engine)
    return (df.to_html())


@app.route('/search_data')
def search_data():
    return render_template('search_data.html')

@app.route('/search_data_column', methods=["GET", "POST"])
def search_data_column():
    search_data_py = request.form.get('search_column_html')
    engine = create_engine('sqlite:///db.sqlite')
    df = pd.read_sql_table('member', engine, columns=[f'{search_data_py}'])
    return (df.to_html())

@app.route('/search_data_row', methods=["GET", "POST"])
def search_data_row():
    search_column_py = request.form.get('search_column_row_html')
    search_row_py = request.form.get('search_row_html')
    engine = create_engine('sqlite:///db.sqlite')
    query = f"SELECT * FROM member WHERE {search_column_py}='{search_row_py}'"
    df = pd.read_sql(query, engine)
    return (df.to_html())

@app.route('/change_data')
def change_data():
    return render_template('change_data.html')

@app.route('/change_data_post', methods=["GET", "POST"])
def change_data_post():
    change_move_py = request.form.get('change_move_html')
    change_after_py = request.form.get('change_after_html')
    engine = create_engine('sqlite:///db.sqlite')
    query = f"ALTER TABLE member MODIFY {change_move_py} TEXT AFTER {change_after_py}"
    df = pd.read_sql(query, engine)
    return(df.to_html())

@app.route('/delete_data')
def delete_data():
    return render_template('delete_data.html')
'''
@app.route('/delete_data_post', methods=["GET", "POST"])
def delete_data_post():
    row_number_py = (request.form.get('row_number_html'))
    engine = sqlite3.connect("./db.sqlite")
    df = pd.read_sql_query("SELECT * FROM member", engine)
    df.drop(column=row_number_py)
    df.to_sql(name='member', con=engine, index=False, if_exists='replace')
    df = pd.read_sql_query("SELECT * FROM member", engine)
    return (df.to_html())
'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
