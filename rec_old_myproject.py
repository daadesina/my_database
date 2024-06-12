#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, url_for, request, redirect
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pymysql

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#        'mysql+pymysql://' + os.path.join(basedir, 'my_datab')

#Create a connection and a database
db = pymysql.connections.Connection(
        host='localhost',
        user='adesina',
        password='ab702810'
        )

print (db)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
cursor.execute("USE my_database")
#cursor.close()
#db.close()



#Configuring the Flask app to connect to the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adesina:ab702810@localhost/my_database'
#engine = create_engine('mysql+pymysql://my_database')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating an instance of the SQLAlchemy class
db = SQLAlchemy(app)

#with app.app_context():
#        db.create_all()

main = Blueprint('main', __name__)
main_blueprint = main
app.register_blueprint(main_blueprint)

#create the database table
class Member(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.VARCHAR(100))
    nickname = db.Column(db.VARCHAR(100))
    gender = db.Column(db.VARCHAR(100))
    religion = db.Column(db.VARCHAR(100))
    month_of_birth = db.Column(db.VARCHAR(100))
    date_of_birth = db.Column(db.VARCHAR(100))
    department = db.Column(db.VARCHAR(100))
    school = db.Column(db.VARCHAR(100))
    level_in_school = db.Column(db.VARCHAR(100))
    date_of_birth = db.Column(db.VARCHAR(100))
    paternal_state_of_origin = db.Column(db.VARCHAR(100))
    maternal_state_of_origin = db.Column(db.VARCHAR(100))
    state_of_residence = db.Column(db.VARCHAR(100))
    state_of_nysc = db.Column(db.VARCHAR(100))
    phone_number = db.Column(db.VARCHAR(100))
    marital_status = db.Column(db.VARCHAR(100))
    known_from = db.Column(db.VARCHAR(100))
    digital_skill = db.Column(db.VARCHAR(100))
    non_digital_skill = db.Column(db.VARCHAR(100))
    side_hustle = db.Column(db.VARCHAR(100))
    best_food = db.Column(db.VARCHAR(100))
    best_color = db.Column(db.VARCHAR(100))
    best_friend = db.Column(db.VARCHAR(100))
    favorite_place = db.Column(db.VARCHAR(100))
    hubby = db.Column(db.VARCHAR(100))
    future_dream = db.Column(db.VARCHAR(1000))

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
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')

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


    #copy the database to a csv file
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    query = """SELECT * FROM member;"""
    df = pd.read_sql(query, engine)
    df_csv = df.to_csv('my_database.csv')
    
    return redirect(url_for('index'))

@app.route('/show_data')
def show_data():
    return render_template('show_data.html')

@app.route('/pre_show_data')
def pre_show_data():
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
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
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    df = pd.read_sql_table('member', engine, columns=[f'{search_data_py}'])
    return (df.to_html())

@app.route('/search_data_row', methods=["GET", "POST"])
def search_data_row():
    search_column_py = request.form.get('search_column_row_html')
    search_row_py = request.form.get('search_row_html')
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    query = f"SELECT * FROM member WHERE {search_column_py}='{search_row_py}'"
    df = pd.read_sql(query, engine)
    return (df.to_html())

@app.route('/edit_data')
def edit_data():
    return render_template('edit_data.html')

@app.route('/edit_data_post', methods=["GET", "POST"])
def edit_data_post():
    edit_move_py = request.form.get('edit_move_html')
    edit_after_py = request.form.get('edit_after_html')
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    query = f"ALTER TABLE member MODIFY {edit_move_py} VARCHAR(100) AFTER {edit_after_py}"
    try:
        pd.read_sql(query, engine)
    finally:
        #copy the database to a csv file
        engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
        query = """SELECT * FROM member;"""
        df = pd.read_sql(query, engine)
        df_csv = df.to_csv('my_database.csv')
        return redirect(url_for('pre_show_data'))

@app.route('/update_data_post', methods=["GET", "POST"])
def update_data_post():
    update_select_column_py = request.form.get('update_select_column_html')
    update_search_id_py = request.form.get('update_search_id_html')
    update_text_py = request.form.get('update_text_html')
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    query = f"UPDATE member SET gender = 'male'"
    cursor.execute(query)
    db.commit()
    #try:
    #df = pd.read_sql(query, engine)
    '''    
    finally:
        #copy the database to a csv file
        engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
        query = """SELECT * FROM member;"""
        df = pd.read_sql(query, engine)
        df_csv = df.to_csv('my_database.csv')
    '''
    return redirect(url_for('pre_show_data'))





    '''
    update_select_column_py = request.form.get('update_select_column_html')
    update_search_id_py = request.form.get('update_search_id_html')
    update_text_py = request.form.get('update_text_html')
    engine = create_engine('mysql+pymysql://adesina:ab702810@localhost/my_database')
    query = f"UPDATE member SET {update_select_column_py} = '{update_text_py}' WHERE id = 1"
    pd.read_sql(query, engine)
    return redirect(url_for('pre_show_data'))
    '''

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
    return ('Process Sucessful')
'''

#cursor.close()
#db.close()
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
