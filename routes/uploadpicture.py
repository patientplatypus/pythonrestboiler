from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import time

# from main import app
# from CORSFIX import crossdomain

print('inside the uploadpicture.py file')
uploadpicture_api = Blueprint('uploadpicture_api', __name__)

@uploadpicture_api.route('/uploadpicture', methods=['POST'])
def uploadpicture():
    print('inside uploadpicture def')
    if request.method=='POST':
        conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'SELECT * FROM logins WHERE username = %s'
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        data = cur.fetchall()
        print(data)
        dataclean = data[0]
        print(dataclean[3])
        millisecondtime =  time.time() * 1000
        sql = 'INSERT INTO "pictures" (URLADDRESS, BOUGHTFOR, SOLDFOR, CURRENTPRICE, PICTUREID, USERREF) VALUES (%s,  %s, %s, %s, %s, %s)'
        params = (request.json['pictureurl'], -1, -1, -1, millisecondtime, dataclean[3])
        cur.execute(sql, params)
        conn.commit()
        conn.close()
        return jsonify({'picture': params})
        # if len(data) > 0:
        #     dataclean = data[0]
        #     databasepassword = dataclean[1]
        #     if databasepassword == request.json['password']:
        #         return 'passwordsmatch'
        #     if databasepassword != request.json['password']:
        #         return 'passwordsdontmatch'
        # if len(data) == 0:
        #     return 'usernamenotfound'
