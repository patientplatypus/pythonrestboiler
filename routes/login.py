from models.todo import TODOS
from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname


# from main import app
# from CORSFIX import crossdomain

print('inside the login.py file')
login_api = Blueprint('login_api', __name__)

@login_api.route('/login', methods=['POST'])
def login():
    print('inside login def')
    if request.method=='POST':
        conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'SELECT * FROM logins WHERE username = %s'
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        data = cur.fetchall()
        conn.close()
        if len(data) > 0:
            dataclean = data[0]
            databasepassword = dataclean[1]
            if databasepassword == request.json['password']:
                return 'passwords match'
            if databasepassword != request.json['password']:
                return 'passwords dont match'
        if len(data) == 0:
            return 'user name not found'
