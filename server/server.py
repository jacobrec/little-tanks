import tornado.websocket
import tornado.ioloop
import tornado.web

from tank import Tank


tanks = []


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("a client joined")
        tanks.append(Tank(
            self, (0, 0, 0), (0, 0)
        ))

    def on_message(self, data):
        pass

    def on_close(self):
        print("a client left")
        for tank in tanks:
            if self is tank.conn:
                tanks.remove(tank)
                break
