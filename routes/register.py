
from models.todo import TODOS
from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import time


print('inside the register.py file')
register_api = Blueprint('register_api', __name__)

@register_api.route('/register', methods=['POST'])
def register():
    print('inside register def')
    if request.method=='POST':
        conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'SELECT * FROM logins WHERE username = %s'
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        data = cur.fetchall()
        conn.close()
        if len(data) == 0:
            conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
            cur = conn.cursor()
            millisecondtime =  time.time() * 1000
            sql = 'INSERT INTO "logins" (USERNAME, PASSWORD, TOTALMONEY, USERID) VALUES (%s,  %s, %s, %s)'
            params = (request.json['name'], request.json['password'], 100, millisecondtime)
            cur.execute(sql, params)
            conn.commit()
            conn.close()
            return 'usersuccessfullyadded'
        if len(data) > 0:
            return 'useralreadyexists'
