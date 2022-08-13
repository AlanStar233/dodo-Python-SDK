import json

import Public_Headers
from Loghelper import log
import ErrorCode
import requests

# 获取 WebSocket 地址
def GetWebSocketConnection():
    # 预定义 URL 和 公共头
    URL = "https://botopen.imdodo.com/api/v1/websocket/connection"
    public_headers = Public_Headers.Headers

    # 发送请求及 json 格式化处理
    websocket_info = requests.post(URL, headers=public_headers)
    websocket_info = websocket_info.text
    websocket_info = json.loads(websocket_info)

    # 数据解析
    status = str(websocket_info["status"])
    print("获取websocket地址状态:" + ErrorCode.dodo_code(str(status)))
    if status != "0":
        log.info("状态码:" + str(status))
        log.info("状态码解释:" + ErrorCode.dodo_code(str(status)))  # 打印状态解释
    else:
        endpoint = websocket_info["data"]["endpoint"]
        # print("endpoint: ", endpoint)   # 调参用
        # 返回 endpoint
        return endpoint


if __name__ == "__main__":
    print(GetWebSocketConnection())
