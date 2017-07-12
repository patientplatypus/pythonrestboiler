from models.todo import TODOS
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

print('inside the retrievepictures.py file')
retrievepictures_api = Blueprint('retrievepictures_api', __name__)

@retrievepictures_api.route('/retrievepictures', methods=['POST'])
def retrievepictures():
    print('inside retrievepictures def')
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
        datasearch = dataclean[3]
        sql = 'SELECT * FROM pictures WHERE userref = %s'
        params = (datasearch,)
        cur.execute(sql, params)
        picturedata = cur.fetchall()
        print(picturedata)
        conn.commit()
        conn.close()
        return jsonify({'pictures': picturedata})
