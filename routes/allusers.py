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
# userref name pictureurl currentprice

print('inside the allusers.py file')
allusers_api = Blueprint('allusers_api', __name__)

@allusers_api.route('/allusers', methods=['POST'])
def allusers():
    print('inside allusers def')
    if request.method=='POST':
        conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'SELECT * FROM logins'
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        print(data)
        returndata = []
        for x in range(0,len(data)):
            returndata.append(data[x][0])
        return jsonify({'allusers': returndata})
