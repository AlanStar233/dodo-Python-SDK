import json

# ./config/bot_Info.json 文件检测
def config_status():
    with open('./config/bot_Info.json', "r", encoding="UTF-8") as doc:
        info = doc.read()
        info = json.loads(info)
        clientId = info["clientId"]
        token = info["token"]
        if clientId == "" or token == "":
            type = -1
        else:
            type = 0
        return type

# 从 json 中获取 clientId
def get_clientId():
    if config_status() == 0:
        with open("config/bot_Info.json", mode="r", encoding="UTF-8") as doc:
            info = doc.read()
            info = json.loads(info)
            clientId = info["clientId"]
        return clientId
    else:
        pass

# 从 json 中获取 token
def get_token():
    if config_status() == 0:
        with open("config/bot_Info.json", mode="r", encoding="UTF-8") as doc:
            info = doc.read()
            info = json.loads(info)
            token = info["token"]
        return token
    else:
        pass

# 拼接 Authorization 以组合公共请求头 -> ./Public_Headers.py
def combine_Authorization():
    Authorization = "Bot " + get_clientId() + "." + get_token()
    return Authorization
