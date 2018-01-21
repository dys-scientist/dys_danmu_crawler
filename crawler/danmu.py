#encoding=utf8
from ws4py.client.threadedclient import WebSocketClient
import json


class DanmuClient(WebSocketClient):
    def opened(self):
        pass

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        danmus = json.loads(str(m))
        print(danmus)

if __name__ == '__main__':
    room_id = 2241164   # 德云色房间ID

    try:
        ws = DanmuClient('ws://mbgows.plu.cn:8805/?room_id=%d&batch=1&group=0&connType=1' % room_id)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
