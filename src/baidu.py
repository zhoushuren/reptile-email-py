
# encoding=utf-8
import re
import sys
import time
import json
import requests
from lxml import html
from mongo import Url,setEmailOne

from request import getBaidu
def main():
    url = Url()
    # newUrl = 'https://tieba.baidu.com/p/4918734951?pn=2' # test
    newUrl = url.getNewUrl(1)
    # print newUrl
    s,nextUrl = getBaidu(newUrl)
    # print s
    # print nextUrl

    now = int(time.time())
    # data = []
    for item in s:
        dict = {
            "email": item,
            "time": now,
            "source": newUrl,
            "send":0,
            "send_time": 0
        }
        # data.append(dict)
        setEmailOne(dict)

    url.setNewUrl(nextUrl);

# main()

while(True):
    time.sleep(1)
    main()
  #   surl = startUrl.split('?')
  #   startUrl = surl[0]
  #   print startUrl
  #   s = set()  # 存放结果的集合
  #   pageList = []  # 分页的url
  #   result = req(startUrl,s,pageList)
  #
  #   if len(pageList) >0:
  #       for val in pageList:
  #           req(val,s,pageList)
  #
  # #  print s
  #   print 'count:' + str(len(s)) + ''
  #   data_email = []
  #   now = int(time.time())
  #
  #   last_page = startUrl
  #   if  len(pageList ) >0:
  #       last_page =  pageList[-1]
  #
  #   for item in s:
  #       dict = {
  #           "_email": item,
  #           "time": now,
  #           "status": 0,
  #           "source": 'tieba',
  #           "last_page":last_page       # 最后一页
  #       }
  #
  #       data_email.append(dict)
  #
  #   return data_email