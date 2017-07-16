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

print('inside the deletepicture.py file')
deletepicture_api = Blueprint('deletepicture_api', __name__)

@deletepicture_api.route('/deletepicture', methods=['POST'])
def deletepicture():
    print('inside deletepicture def')
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
        sql = 'DELETE FROM pictures WHERE pictureid = %s'
        params = (request.json['picturid'],)
        print('deleted picture with pictureid ', request.json['pictureid'])
        cur.execute(sql, params)
        conn.commit()
        conn.close()
        return 'picturedeleted'
        # print(dataclean)
        # if (dataclean[2]>=request.json['cost']):
        #     newtotalmoney = dataclean[2]-request.json['cost']
        #     sql = 'UPDATE logins SET totalmoney = %s WHERE username = %s'
        #     params = (newtotalmoney, request.json['name'],)
        #     cur.execute(sql, params)
        #     conn.commit()
        #     millisecondtime =  time.time() * 1000
        #     sql = 'INSERT INTO "pictures" (URLADDRESS, BOUGHTFOR, SOLDFOR, CURRENTPRICE, PICTUREID, USERREF) VALUES (%s,  %s, %s, %s, %s, %s)'
        #     params = (request.json['pictureurl'], -1, -1, -1, millisecondtime, dataclean[3])
        #     cur.execute(sql, params)
        #     conn.commit()
        #     conn.close()
        #     return jsonify({'picture': params, 'totalmoney': newtotalmoney})
        # if (dataclean[2]<request.json['cost']):
        #     return 'youdonthaveenoughmoney'

        # print(dataclean[3])
        # return 'dummyforthemoment'
        # millisecondtime =  time.time() * 1000
        # sql = 'INSERT INTO "pictures" (URLADDRESS, BOUGHTFOR, SOLDFOR, CURRENTPRICE, PICTUREID, USERREF) VALUES (%s,  %s, %s, %s, %s, %s)'
        # params = (request.json['pictureurl'], -1, -1, -1, millisecondtime, dataclean[3])
        # cur.execute(sql, params)
        # conn.commit()
        # conn.close()
        # return jsonify({'picture': params})
