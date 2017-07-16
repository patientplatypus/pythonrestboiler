from flask_restful import abort, reqparse, Resource
from marshmallow import Schema, fields, ValidationError, pre_load
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from os.path import join, dirname
import threading
from time import sleep
import math
import urlparse
# DB_DRIVER=postgresql
# DB_HOST=localhost
# DB_USER=patientplatypus
# DB_PASSWORD=Fvnjty0b
# DB_NAME=pictureswapper

class Inflate:
    threads = []
    def __init__(self, s):
        self.s = s
    def printtest(self):
        print('insided the printtest for inflation')
    def inflatemethod(self):
        while 1 > 0:
            # conn = psycopg2.connect(database = os.environ.get('DB_NAME'), user = os.environ.get('DB_USER'), password = os.environ.get('DB_PASSWORD'))

            urlparse.uses_netloc.append("postgres")
            url = urlparse.urlparse(os.environ["DATABASE_URL"])

            conn = psycopg2.connect(
                database=url.path[1:],
                user=url.username,
                password=url.password,
                host=url.hostname,
                port=url.port
            )



            # conn = psycopg2.connect(database = 'pictureswapper', user = 'patientplatypus', password = 'Fvnjty0b')
            cur = conn.cursor()
            sql = 'SELECT * FROM logins'
            cur.execute(sql)
            conn.commit()
            userdata = cur.fetchall()
            userdataclean = userdata[0]
            print('this is the value of userdataclean ', userdataclean)
            print('this is the value of userdata ', userdata)
            usermoney = []
            totalmoney = 0
            for x in range(0,len(userdata)):
                userdict = {}
                userdict['name'] = userdata[x][0]
                userdict['money'] = userdata[x][2]
                usermoney.append(userdict)
            sortedusers = sorted(usermoney, key=lambda k: k['money'])
            print('sortedusers before adding: ', sortedusers)
            for x in range(0, len(sortedusers)):
                if 100 * x / len(sortedusers) <= 20 and sortedusers[x]['money']<sortedusers[int(math.ceil(0.2*len(sortedusers)))]['money']:
                    sortedusers[x]['money'] = sortedusers[x]['money'] + 1
            print('sortedusers after adding: ', sortedusers)
            # now send to daterbase
            for x in range(0, len(sortedusers)):
                sql = 'UPDATE logins SET totalmoney = %s WHERE username = %s'
                params = (sortedusers[x]['money'], sortedusers[x]['name'],)
                cur.execute(sql, params)
                conn.commit()
            conn.close()
            sleep(300000)
    def timermethod(self):
        h="hello there "
        t = threading.Thread(target=self.inflatemethod, args=())
        t.start()


#     totalmoney = totalmoney + userdata[x][2]
# for x in range(0, len(usermoney)):
#     usermoney[x]['percentage'] = 100 * usermoney[x]['money'] / totalmoney
# print('***** values after first look *****')
# print('usermoney ', usermoney)
# print('totalmoney ', totalmoney)
#
# for x in range(0, len(usermoney)):
#     if usermoney[x]['percentage'] <= 20:
#         sql = 'UPDATE logins SET totalmoney = %s WHERE username = %s'
#         newtotalmoney = usermoney[x]['money']+10
#         params = (newtotalmoney, usermoney[x]['name'],)
#         cur.execute(sql, params)
#         conn.commit()
#
# sleep(5)
#
# sql = 'SELECT * FROM logins'
# cur.execute(sql)
# conn.commit()
# userdatanew = cur.fetchall()
# usermoneynew = []
# totalmoneynew = 0
# for x in range(0,len(userdatanew)):
#     userdict = {}
#     userdict['name'] = userdatanew[x][0]
#     userdict['money'] = userdatanew[x][2]
#     usermoneynew.append(userdict)
#     totalmoneynew = totalmoneynew + userdatanew[x][2]
# for x in range(0, len(usermoneynew)):
#     usermoneynew[x]['percentage'] = 100 * usermoneynew[x]['money'] / totalmoney
#
#
# print('***** values after add money *****')
# print('usermoneynew ', usermoneynew)
# print('totalmoneynew ', totalmoneynew)
#
# print('***** the total number of users *****')
# print('total number of users: ', len(userdata))
#
# conn.close()

#
# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

#
# class Inflate:
#     # def __init__(self, profitorloss, listname, itemname, itemdescription):
#     #     self.profitorloss = profitorloss
#     #     self.listname = listname
#     #     self.itemname = itemname
#     #     self.itemdescription = itemdescription
#     threads = []
#     def __init__(self, s):
#         self.s = s
#     def printtest(self):
#         print('insided the printtest for inflation')
#     def hello(self, h):
#         print h + self.s
#     def timermethod(self):
#         h="hello there "
#         for i in range(5):
#             t = threading.Thread(target=self.hello, args=(h,))
#             t.start()
            # sleep(2)
        # while 1>0:
        #     t = threading.Timer(2, self.hello, [h])
        #     t.start()
        #     sleep(2)
            # time.sleep(2)

        # print "Hi"
        # i=10
        # i=i+20
        # print i

# class Typewriter(threading.Thread):
#     def __init__(self, your_string):
#         threading.Thread.__init__(self)
#         self.my_string = your_string
#
#     def run(self):
#         for char in self.my_string:
#             libtcod.console_print(0,3,3,char)
#             time.sleep(50)


# import threading
#
# def worker():
#     """thread worker function"""
#     print 'Worker'
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()


#!/usr/bin/python
#
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print "Starting " + self.name
#       print_time(self.name, self.counter, 5)
#       print "Exiting " + self.name
#
# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print "%s: %s" % (threadName, time.ctime(time.time()))
#       counter -= 1
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# print "Exiting Main Thread"

# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
