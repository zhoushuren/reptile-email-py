# 爬取邮件的爬虫

目前只支持爬取百度贴吧。

* 部署方式：
```
pip install request lxml pymongo

```

爬取的数据采用mongodb存储。支持分页爬取，非重复爬取。

* 实现逻辑

指定 url 存入urllib集合。脚本自动按时间生序读取Url。遍历Url里的Email。

具体请看代码

server.py 目前没有用。不支持接口调用。