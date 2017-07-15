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

print('inside the buyfromothers.py file')
buyfromothers_api = Blueprint('buyfromothers_api', __name__)

@buyfromothers_api.route('/buyfromothers', methods=['POST'])
def buyfromothers():
    print('inside buyfromothers def')
    if request.method=='POST':
        conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))
        cur = conn.cursor()
        sql = 'SELECT * FROM logins WHERE username = %s'
        print('this is the name value: ', request.json['name'])
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        userdata = cur.fetchall()
        # print('this is the userdata', userdata)
        # print('this is the type of request.json[othername]', type(request.json['othername']))
        # if type(request.json['othername'])==type(1):
        #     print('hello there sailor')
        if  type(request.json['othername'])==type(1):
            sql = 'SELECT * FROM logins WHERE userid = %s'
        if  type(request.json['othername'])!=type(1):
            sql = 'SELECT * FROM logins WHERE username = %s'
        params = (request.json['othername'],)
        cur.execute(sql, params)
        conn.commit()
        otheruserdata = cur.fetchall()
        print('this is the otheruserdata', otheruserdata)
        userclean = userdata[0]
        otheruserclean = otheruserdata[0]
        print('this is the value of userclean[2]', userclean[2])
        print('this is the value of the price', request.json['price'])
        print('this is the value of the the difference', userclean[2] - int(request.json['price']))
        if userclean[2]>=int(request.json['price']):
            lessmoney = userclean[2] - int(request.json['price'])
            moremoney = otheruserclean[2] + int(request.json['price'])
            sql = 'UPDATE pictures SET userref = %s, currentprice = %s WHERE urladdress = %s'
            params = (userclean[3], -1, request.json['pictureurl'],)
            cur.execute(sql, params)
            conn.commit()
            sql = 'UPDATE logins SET totalmoney = %s WHERE username = %s'
            params = (lessmoney, request.json['name'],)
            cur.execute(sql, params)
            conn.commit()
            if type(request.json['othername'])==type(1):
                sql = 'UPDATE logins SET totalmoney = %s WHERE userid = %s'
            if type(request.json['othername'])!=type(1):
                sql = 'UPDATE logins SET totalmoney = %s WHERE username = %s'
            params = (moremoney, request.json['othername'],)
            cur.execute(sql, params)
            conn.commit()
            conn.close()
            return 'purchasemadesucessfully'
        if userclean[2]<int(request.json['price']):
            return 'youdonthaveenoughmoney'
        # sql = 'SELECT * FROM pictures WHERE pictureurl = %s'
        # params = (request.json['pictureurl'],)
        # cur.execute(sql, params)
        # conn.commit()
        # picturedata = cur.fetchall()

        # return 'dummyforthemoment'





        # print(data)
        # dataclean = data[0]
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
