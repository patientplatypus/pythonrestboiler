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





# i = Inflate()
# i.timermethod('pants')
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks
#
# e.tricks

# typer = Typewriter('hello there sailor')
# typer.start()



i = Inflate('pants')
i.timermethod()


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (os.environ.get('DB_DRIVER'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'), os.environ.get('DB_NAME'))

# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379'
# )
# celery = make_celery(app)

# @celery.task()
# def add_together(a, b):
#     return a + b


# result = add_together.delay(23, 42)
# result.wait()

db = SQLAlchemy()

db.app = app
db.init_app(app)
# Create tables if they don't already exist
db.create_all()

conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
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



if __name__ == '__main__':
    app.run(debug=True)
