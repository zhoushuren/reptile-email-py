
#

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/get_email", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()


