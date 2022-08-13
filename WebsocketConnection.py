# -*- coding: UTF-8 -*-
import json
import time
from datetime import datetime

import websocket
import GetWebSocketConnection
import SendPersonalMessage

try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    # binary 解码转 UTF-8 部分
    message = str(message, "utf-8")
    message = message.strip("b").strip("'")
    print("[Get message]:", message)

    # json 解析 -> ./res/ws_message_struct.json   (仅作为示例)
    message = json.loads(message)

    # dodo 号
    dodoId = message["data"]["eventBody"]["dodoId"]
    # 文字内容
    content = message["data"]["eventBody"]["messageBody"]["content"]
    # 消息类型 -> ./res/ws_message_type.json
    messageType = message["data"]["eventBody"]["messageType"]
    # 消息ID
    messageId = message["data"]["eventBody"]["messageId"]
    # 用户名
    nickName = message["data"]["eventBody"]["personal"]["nickName"]
    # 性别
    sex = message["data"]["eventBody"]["personal"]["sex"]
    # eventType 类型解释 -> ./res/ws_message_type.json
    eventType = message["data"]["eventType"]
    # 时间戳   (下方 sendTime 提供了源数据 13 位 时间戳的标准时间转换，可选)
    timestamp = message["data"]["timestamp"]
    # sendTime = time.strftime('%Y{Y}%m{m}%d{d} %H:%M:%S', time.localtime(timestamp)).format(Y='年',
    #                                                                                        m='月',
    #                                                                                        d='日')  # 10位时间戳转换, 此处不适用
    sendTime = datetime.fromtimestamp(timestamp / 1000.0).strftime("%Y{Y}%m{m}%d{d} %H:%M:%S").format(Y='年',
                                                                                                      m='月',
                                                                                                      d='日')  # 13位时间戳转换
    # 打印监听到的消息
    print("\033[92m[message]\033[0m ", messageId, "\n"
          " dodo ID: ", dodoId, "\n",
          "nickName: ", nickName, "\n",
          "sex: ", sex, "\n",
          "content: ", content, "\n",
          "eventType: ", eventType, "\n",
          "messageType: ", messageType, "\n",
          "time:", sendTime, "\n"
          )
    # 定义回复内容
    reply_content = "啊哈！本bot收到你的消息辣!\n你说的是 ↓\n " + content
    # 调用 sendPersonalMessage.send() 方法发送私信
    SendPersonalMessage.send(dodoId=dodoId, messageType=1, content=reply_content)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Websocket Closed!")

def on_open(ws):
    def run(*args):
        ws.send("hello")
        time.sleep(1)
        ws.close()

    thread.start_new_thread(run(), ())

def on_ping(ws, message):
    print("\033[31m[Heartbeat]\033[0m Now got a Ping, Pong have sent to server...")

def on_pong(ws, message):
    print("\033[31m[Heartbeat]\033[0m Now got a Pong, Ping have sent to server...")


if __name__ == "__main__":
    # 调用 GetWebSocketConnection.GetWebSocketConnection() 方法来获取wss地址
    ws_address = GetWebSocketConnection.GetWebSocketConnection()
    # 创建 webSocketApp 连接
    ws = websocket.WebSocketApp(ws_address,
                                on_message=on_message,
                                on_ping=on_ping,
                                on_pong=on_pong,
                                on_error=on_error,
                                on_close=on_close)
    # 打印本次获得的 wss 地址
    print("[Websocket address] : ", ws_address)
    # 运行
    ws.open = on_open
    # 连接保持, 根据官方文档要求30秒发送一次心跳(Heartbeat), 超时时间自定为10秒
    ws.run_forever(ping_interval=30, ping_timeout=10, ping_payload="Ping payload")
