from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import time
import urlparse

# from main import app
# from CORSFIX import crossdomain
# userref name pictureurl currentprice

print('inside the changeprice.py file')
changeprice_api = Blueprint('changeprice_api', __name__)

@changeprice_api.route('/changeprice', methods=['POST'])
def changeprice():
    print('inside changeprice def')
    if request.method=='POST':
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["postgresql-rugged-56632"])

        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        # conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'UPDATE pictures SET currentprice = %s WHERE pictureid = %s'
        params = (request.json['currentprice'], request.json['pictureid'],)
        print('this is the value of the params ', params)
        cur.execute(sql, params)
        conn.commit()
        # data = cur.fetchall()
        # print("the value of the data is ", data)
        conn.close()
        return 'priceset'
