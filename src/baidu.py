
# encoding=utf-8
import time
from mongo import Url,setEmailOne

from request import getBaidu
def main():
    url = Url()
    # newUrl = 'https://tieba.baidu.com/p/4918734951?pn=2' # test
    newUrl = url.getNewUrl(1)
    if(newUrl is None):
        return

    s,nextUrl = getBaidu(newUrl)

    now = int(time.time())

    for item in s:
        dict = {
            "email": item,
            "time": now,
            "source": newUrl,
            "send":0,
            "send_time": 0
        }
        setEmailOne(dict)

    url.setNewUrl(nextUrl);

# main()    #保守的爬，100秒一次，这里可以控制速度
while(True):
    time.sleep(100)
    main()
