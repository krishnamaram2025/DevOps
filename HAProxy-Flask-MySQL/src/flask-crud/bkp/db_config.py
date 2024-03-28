from app import app
from flask_mysqldb import MySQL
from flask import Flask, request, render_template
app = Flask(__name__)
#mysql = MySQL()
#configure db
app.config['MYSQL_DATABSE_HOST'] = '192.168.2.7'
app.config['MYSQL_DATABSE_USER'] = 'cloud'
app.config['MYSQL_DATABSE_PASSWORD'] = 'Cloud_123'
app.config['MYSQL_DATABSE_DB'] = 'cloudstones'
mysql=MySQL(app)
