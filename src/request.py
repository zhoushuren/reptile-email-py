# encoding=utf-8
import re
import sys
import time
import json
import requests
from lxml import html
import urllib3
urllib3.disable_warnings()
def req(startUrl,s,pageList):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': 'TIEBA_USERTYPE=23fdbb361380878070691806; bdshare_firstime=1474861285905; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1482850292,1482850327,1482850532,1482850569; BDUSS=lBURmlySTdock5UclFLLU85ZE54NVp5bklBSy1yflhBQTZVUGtFbkh4b2ZoSmxZSVFBQUFBJCQAAAAAAAAAAAEAAADBLM4WwMPSttfT0rvGrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB~3cVgf93FYM; STOKEN=557107e8dd3128a8347e7d06d0c7cb09df019f2b9c8c8db9830ee13a6abab4f4; TIEBAUID=83f4b7179f8aeee39cb626b5; BAIDUID=C17787A1E42B2D4EF1ACF2655D088176:FG=1; PSTM=1485230263; BIDUPSID=E4C79AC24E4807BC0807F3ABE82BD396; MCITY=-289%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; H_PS_PSSID=1429_21094_21942_21801_22026; wise_device=0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    }


    r = requests.get(
        startUrl,
        headers=header,verify=False)

    tree = html.fromstring(r.content)

    pageListHtml = tree.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[1]/a/@href')   # 选取分页
    pageNumHtml = tree.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[2]/span[2]/text()')   # 选取分页数，贴吧太变态，选取分页数才是最明智的

    pageNum = int (pageNumHtml[0])

    if len(pageList) == 0:
        if pageNum > 1:
            startUrl_model = startUrl.split('=')
            _startUrl_model = startUrl_model[0]

            while pageNum:
                continueUrl = _startUrl_model + '?pn=' + str(pageNum)
              #  print continueUrl
                pageList.append(continueUrl)
                pageNum = pageNum - 1

    buyers = tree.xpath('//*[@id="j_p_postlist"]/div[6]/div[2]/div[1]/cc/text()')   # 主要的内容
   # print buyers
    # print buyers
    regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)

    result = str(re.findall(regex, r.content)).replace("']", '').replace("['", '').replace("[]", '').replace("', '", ',').replace("[u'", '').replace("u", '')

    # print result
    res = result.split(',')
    print res

    for val in res:
        if(val not in s):
            s.add(val)


def getBaidu(url):
    text = reqBaidu(url)
    s, pageNum =  parseBaidu(text)
    nextUrl = url

    startUrl_model = url.split('=')

    if(len(startUrl_model) == 2 and  pageNum <= int(startUrl_model[1])):
        return s, nextUrl

    if(pageNum>1 ):

        _startUrl_model = startUrl_model[0]

        if(len(startUrl_model) ==1):
            nextUrl = _startUrl_model + '?pn=' + str(2)
        elif(startUrl_model[1] != pageNum):
            num = int(startUrl_model[1])
            num = num +1
            nextUrl =   _startUrl_model + '=' + str(num)

    return s,nextUrl



def reqBaidu(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': 'TIEBA_USERTYPE=23fdbb361380878070691806; bdshare_firstime=1474861285905; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1482850292,1482850327,1482850532,1482850569; BDUSS=lBURmlySTdock5UclFLLU85ZE54NVp5bklBSy1yflhBQTZVUGtFbkh4b2ZoSmxZSVFBQUFBJCQAAAAAAAAAAAEAAADBLM4WwMPSttfT0rvGrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB~3cVgf93FYM; STOKEN=557107e8dd3128a8347e7d06d0c7cb09df019f2b9c8c8db9830ee13a6abab4f4; TIEBAUID=83f4b7179f8aeee39cb626b5; BAIDUID=C17787A1E42B2D4EF1ACF2655D088176:FG=1; PSTM=1485230263; BIDUPSID=E4C79AC24E4807BC0807F3ABE82BD396; MCITY=-289%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; H_PS_PSSID=1429_21094_21942_21801_22026; wise_device=0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    }
    # return requests.get(url,headers=header,verify=False)
    return requests.get(url,headers=header)

def parseBaidu(text):
    tree = html.fromstring(text.content)
    pageNumHtml = tree.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[2]/span[2]/text()')   # 选取分页数，贴吧太变态，选取分页数才是最明智的
    pageNum = int(pageNumHtml[0])

    regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)

    result = str(re.findall(regex, text.content)).replace("']", '').replace("['", '').replace("[]", '').replace("', '", ',').replace("[u'", '').replace("u", '')

    # print result
    res = result.split(',')
    s = set()
    for val in res:
        if(val not in s):
            s.add(val)
    return s,pageNum