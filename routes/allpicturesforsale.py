from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import time


print('inside the allpicturesforsale.py file')
allpicturesforsale_api = Blueprint('allpicturesforsale_api', __name__)

@allpicturesforsale_api.route('/allpicturesforsale', methods=['POST'])
def allpicturesforsale():
    print('inside allpicturesforsale def')
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
        sql = 'SELECT * FROM logins WHERE username =  %s'
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        datauser = cur.fetchall()
        datauserclean = datauser[0]
        userref = datauserclean[3]
        sql = 'SELECT * FROM pictures WHERE userref !=  %s AND CAST(currentprice as int) != %s'
        params = (userref,-1,)
        cur.execute(sql, params)
        picturedata = cur.fetchall()
        print('this is the allpicturesforsale data')
        print(picturedata)
        conn.commit()
        conn.close()
        return jsonify({'allpicturesforsale': picturedata})
