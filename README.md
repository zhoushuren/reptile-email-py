# 爬取邮件的爬虫

目前只支持爬取百度贴吧。

* 部署方式：
```
pip install request lxml pymongo

```

爬取的数据采用mongodb存储。支持分页爬取，非重复爬取。

* 实现逻辑

指定 url 存入urllib集合。脚本自动按时间生序读取Url。遍历Url里的Email。

当爬到最后一页的时候把本urlupdate成最后一页的url，并把updatetime更新。下次爬取按照updatetime升序取URL。

email和url有唯一索引，不必担心email结果重复

控制爬取时间请在
```
while(True):
    time.sleep(100)
    main()

```
设置休眠时间，或者把这个while去掉采用Linux的conretab实现定时爬取
server.py 目前没有用。不支持接口调用。