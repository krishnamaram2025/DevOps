import sys
#sys.path.insert(0,'.')
import pymysql
#import mysql
#from app import app as application
#app = application
from tables import Results
#from db_config import MySQL
from flask import flash, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, request, render_template
from flask_mysqldb import MySQL
application = Flask(__name__)

#configure db
application.config['MYSQL_HOST'] = '172.31.26.151'
application.config['MYSQL_USER'] = 'cloud'
application.config['MYSQL_PASSWORD'] = 'Cloud_123'
application.config['MYSQL_DB'] = 'cloudstones'
mysql = MySQL(application)





@application.route('/new_user')
def add_user_view():
    return render_template('add.html')

@application.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        if _name and _email and _password and request.method =='POST':
            _hashed_password = generate_password_hash(_password)
            sql = "INSERT INTO tbl_usr(user_name,user_email,user_password) VALUES(%s,%s,%s)"
            data = (_name,_email,_hashed_password)
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('User added successfully')
            return redirect('/')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@application.route('/')
def add_users():
    conn = None
    cursor = None
    try:
        conn = mysql.connection
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user")
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('users.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@application.route('/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connection
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user where user_id=%s, id")
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return "Error loading #{id}".format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@application.route('/update', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        if _name and _email and _password and request.method =='POST':
            _hashed_password = generate_password_hash(_password)
            sql = "UPDATE tbl_usr SET user_name=%s,user_email=%s,user_password=%s WHERE user_id=%s"
            data = (_name,_email,_hashed_password)
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('User added successfully')
            return redirect('/')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@application.route('/delete/<int:id>')
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user where user_id=%s, (id,)")
        conn.commit()
        flash('User deleted successfully')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
if __name__=="__main__":
    application.run()
