import tornado.websocket
import tornado.ioloop
import tornado.web

from tank import Tank


tanks = []


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("a cleint joined")
        tanks.append(Tank(
            self, (0, 0, 0), (0, 0, 0)
        ))

    def on_message(self, data):
        pass

    def on_close(self):
        print("a client left")
        for tank in tanks:
            if self is tank.conn:
                tanks.remove(tank)
                break


class StaticHandler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        if not url_path or url_path.endswith('/'):
            url_path = url_path + 'index.html'
        return url_path


application = tornado.web.Application([
    (r"/websocket", Handler),
    (r"/(.*)", StaticHandler, {"path": os.getcwd()+"/www"})
])

try:
    print("server starting")
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt:
    print("server exited")
