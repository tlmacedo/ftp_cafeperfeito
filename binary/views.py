from django.urls import reverse_lazy
from django.views.generic import TemplateView

import json
import ssl

import websocket

listSymbols = ['1HZ10V', 'R_10', '1HZ25V', 'R_25', '1HZ50V', 'R_50', '1HZ75V', 'R_75', '1HZ100V', 'R_100']


def on_message(ws, message):
    # print('msg: ' + message)
    jsonData = json.loads(message)
    tick = jsonData['tick']
    quote = tick['quote']

    print(tick)


def on_error(ws, error):
    print('err: ' + error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    for symbol in listSymbols:
        sub_params = {'ticks': symbol, 'subscribe': '1'}
        my_json = json.dumps(sub_params)
        print('my_json: ' + my_json)
        ws.send(my_json)


def open_servidor():
    # if __name__ == "__main__":
    websocket.enableTrace(True)
    host = "wss://ws.binaryws.com/websockets/v3?app_id=23487"
    ws = websocket.WebSocketApp(host,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    # ws.on_open = on_open
    # ws.send("{  \"ticks\": \"R_50\",  \"subscribe\": 1}")
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


class IndexView(TemplateView):
    template_name = 'binary/index.html'
    reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        open_servidor()
        return super(IndexView, self).get_context_data(*args, **kwargs)

    # def open_servidor(self):
    #     # if __name__ == "__main__":
    #     websocket.enableTrace(True)
    #     host = "wss://ws.binaryws.com/websockets/v3?app_id=23487"
    #     ws = websocket.WebSocketApp(host,
    #                                 on_open=on_open,
    #                                 on_message=on_message,
    #                                 on_error=on_error,
    #                                 on_close=on_close)
    #     # ws.on_open = on_open
    #     # ws.send("{  \"ticks\": \"R_50\",  \"subscribe\": 1}")
    #     ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
