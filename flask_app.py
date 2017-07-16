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
from timed.inflation import Inflate
# from timed.inflation import Typewriter
# from timed.inflation import Dog
import threading

# from celeryconfig import make_celery

from urlparse import urlparse



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (os.environ.get('DB_DRIVER'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'), os.environ.get('DB_NAME'))
#
#
# db = SQLAlchemy()
#
# db.app = app
# db.init_app(app)
# # Create tables if they don't already exist
# db.create_all()


# localhost uses this
# conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["postgresql-rugged-56632"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()
q = """CREATE TABLE IF NOT EXISTS logins (
         username  VARCHAR(255),
         password  VARCHAR(255),
         totalmoney bigint,
         userid bigint,
         PRIMARY KEY (userid));"""
cur.execute(q)
conn.commit()
r = """CREATE TABLE IF NOT EXISTS pictures (
         urladdress  VARCHAR(255),
         boughtfor  VARCHAR(255),
         soldfor  VARCHAR(255),
         currentprice VARCHAR(255),
         pictureid bigint,
         userref bigint REFERENCES logins(userid),
         PRIMARY KEY (pictureid, userref));"""
cur.execute(r)
conn.commit()
conn.close()



i = Inflate('pants')
i.timermethod()



print('inide the main file')
from routes.login import login_api
app.register_blueprint(login_api)

from routes.register import register_api
app.register_blueprint(register_api)

from routes.uploadpicture import uploadpicture_api
app.register_blueprint(uploadpicture_api)

from routes.retrievepictures import retrievepictures_api
app.register_blueprint(retrievepictures_api)

from routes.changeprice import changeprice_api
app.register_blueprint(changeprice_api)

from routes.retrieveuserinfo import retrieveuserinfo_api
app.register_blueprint(retrieveuserinfo_api)

from routes.buypictures import buypictures_api
app.register_blueprint(buypictures_api)

from routes.allusers import allusers_api
app.register_blueprint(allusers_api)

from routes.buyfromothers import buyfromothers_api
app.register_blueprint(buyfromothers_api)

from routes.allpicturesforsale import allpicturesforsale_api
app.register_blueprint(allpicturesforsale_api)

from routes.deletepicture import deletepicture_api
app.register_blueprint(deletepicture_api)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# the following works for running on local host
# if __name__ == '__main__':
#     app.run(debug=True)

# the following is recommended to use in order to get this to work on heroku
# (step 7 of here http://kennmyers.github.io/tutorial/2016/03/11/getting-flask-on-heroku.html)
if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)
