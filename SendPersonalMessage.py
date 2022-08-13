import json
import requests
import Public_Headers

# TODO: 私信消息不支持Markdown
def send(dodoId, messageType, content):
    URL = "https://botopen.imdodo.com/api/v1/personal/message/send"
    public_headers = Public_Headers.Headers
    message_data = {
        "dodoId": dodoId,
        "messageType": messageType,
        "messageBody": {
            "content": content
        }
    }

    # 发送请求
    send_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))  # 这里需要dumps
    send_message = send_message.text
    send_message = json.loads(send_message)

    # 数据解析
    # print(send_message)  # 完整输出json
    status = str(send_message["status"])
    status_message = send_message["message"]
    # 消息ID
    messageId = send_message["data"]["messageId"]

    # 打印消息
    print("\033[92m[status]\033[0m 私信消息已回复!\n"
          "status: ", status, "\n"
          "message: ", status_message, "\n"
          "messageId: ", messageId, "\n")


if __name__ == "__main__":
    reply_content = "啊哈！本bot收到你的消息辣!"
    dodoId = 254913173
    send(dodoId=dodoId, messageType=1, content=reply_content)