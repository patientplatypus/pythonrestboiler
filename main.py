from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
from os.path import join, dirname
import sys
import psycopg2
# from CORSFIX import crossdomain

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (os.environ.get('DB_DRIVER'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'), os.environ.get('DB_NAME'))


db = SQLAlchemy()

db.app = app
db.init_app(app)
# Create tables if they don't already exist
db.create_all()

conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
cur = conn.cursor()
q = """CREATE TABLE IF NOT EXISTS logins (
         username  VARCHAR(255),
         password  VARCHAR(255))"""
cur.execute(q)
conn.commit()
conn.close()



print('inide the main file')
from routes.login import login_api
app.register_blueprint(login_api)

from routes.register import register_api
app.register_blueprint(register_api)



@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)
