# encoding=utf-8
from pymongo import *
import pymongo
import time
client = MongoClient()

db = client.kaoshi

collection = db.douban

def mInsert(obj):
    result = collection.insert_many(obj)
    print result

urllib = db.urllib

class Url():
    def __init__(self):
        self.thisUrl = ''

    def getNewUrl(self,type):

        count = urllib.count()
        print count
        if (count== 0):
            print "没有url鸟"
            return

        list = urllib.find({"type":type}).sort("update_time").limit(1)

        # print list[0].get('url')
        self.thisUrl = list[0].get('url')
        return list[0].get('url')

    def setNewUrl(self,newUrl):
        # print self.thisUrl
        # print newUrl
        result = urllib.update({"url": self.thisUrl},{"$set":{"url":newUrl,"update_time":time.time()}})
        print result

def setEmailMany(obj):
    email_lib = db.email_lib
    return email_lib.insert_many(obj)

def setEmailOne(obj):
    email_lib = db.email_lib
    try:
        return email_lib.insert_one(obj)
    except:
        print '重复了'
        print obj.get("email")

def _init():
    result = db.email_lib.create_index([('email', pymongo.ASCENDING),('source', pymongo.ASCENDING)], unique = True)
    print result
    print 'indexCreateSuccess'

_init()