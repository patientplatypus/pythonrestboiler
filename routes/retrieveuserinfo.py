from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import time
from urlparse import urlparse

# from main import app
# from CORSFIX import crossdomain

print('inside the retrieveuserinfo.py file')
retrieveuserinfo_api = Blueprint('retrieveuserinfo_api', __name__)

@retrieveuserinfo_api.route('/retrieveuserinfo', methods=['POST'])
def retrieveuserinfo():
    print('inside retrieveuserinfo def')
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
        sql = 'SELECT * FROM logins WHERE username = %s'
        params = (request.json['name'],)
        cur.execute(sql, params)
        conn.commit()
        data = cur.fetchall()
        dataclean = data[0]
        print(dataclean)
        conn.close()
        return jsonify({'userinfo': dataclean})
