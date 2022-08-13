import json

import requests

import Public_Headers

# 机器人退群
def leave(islandId):
    URL = "https://botopen.imdodo.com/api/v1/bot/island/leave"
    public_headers = Public_Headers.Headers
    message_data = {
        "islandId": islandId
    }

    # 发送请求
    leave_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))  # 这里需要dumps
    leave_message = leave_message.text
    leave_message = json.loads(leave_message)

    # 数据解析
    status = leave_message["status"]
    message = leave_message["message"]

    # 返回 json
    return leave_message


if __name__ == "__main__":
    islandId = 0
    leave(islandId=islandId)