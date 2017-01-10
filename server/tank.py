import json


class Tank:
    def __init__(self, conn, pos, angle):
        self.conn = conn
        self.pos = pos
        self.angle = angle

    def send_update(self):
        self.conn.write_message(self)

    def __str__(self):
        return json.dumps({
            "pos": self.pos,
            "angle": self.angle
        })
