import json

import requests

import Public_Headers

# 获取群列表
def getIslandList():
    URL = "https://botopen.imdodo.com/api/v1/island/list"
    public_headers = Public_Headers.Headers

    # 发送请求
    group_message = requests.post(URL, headers=public_headers)
    group_message = group_message.text
    group_message = json.loads(group_message)

    # 数据解析, 但不输出
    status = group_message["status"]
    message = group_message["message"]

    # 搞个 r 占位, 因为 data 数据体不唯一
    r = 0
    # 群号
    islandId = group_message["data"][r]["islandId"]
    # 群名
    islandName = group_message["data"][r]["islandName"]
    # 群头像
    coverUrl = group_message["data"][r]["coverUrl"]
    # 人数
    memberCount = group_message["data"][r]["memberCount"]
    # 群内在线人数
    onlineMemberCount = group_message["data"][r]["onlineMemberCount"]
    # 默认访问频道ID
    defaultChannelId = group_message["data"][r]["defaultChannelId"]
    # 系统消息频道ID
    systemChannelId = group_message["data"][r]["systemChannelId"]

    # 返回 json
    return group_message

# 获取群信息
def getIslandInfo(islandId):
    URL = "https://botopen.imdodo.com/api/v1/island/info"
    public_headers = Public_Headers.Headers
    message_data = {
        "islandId": islandId
    }

    # 发送请求
    group_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))
    group_message = group_message.text
    group_message = json.loads(group_message)

    try:
        # 数据解析
        status = group_message["status"]
        message = group_message["message"]

        # 群名称
        islandName = group_message["data"]["islandName"]
        # 群封面地址
        coverUrl = group_message["data"]["coverUrl"]
        # 成员数量
        memberCount = group_message["data"]["memberCount"]
        # 群在线成员数量
        onlineMemberCount = group_message["data"]["onlineMemberCount"]
        # 简介 (如果有简介会有这个属性，否则报错)
        description = group_message["data"]["description"]
        # 默认访问频道ID
        defaultChannelId = group_message["data"]["defaultChannelId"]
        # 系统消息频道ID
        systemChannelId = group_message["data"]["systemChannelId"]
        # TODO: 这里 description 在默认为空的情况下 json 会缺失这一属性, 会报错, 错误未记录, 等待补充
    except KeyError:
        print("\033[31m[Error]\033[0m 目标群可能未填写群简介")

    # 返回 json
    return group_message

# 获取群等级信息
def getIslandLevelRankList(islandId):
    URL = "https://botopen.imdodo.com/api/v1/island/level/rank/list"
    public_headers = Public_Headers.Headers
    message_data = {
        "islandId": islandId
    }

    # 发送请求
    group_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))
    group_message = group_message.text
    group_message = json.loads(group_message)

    # 数据解析
    status = group_message["status"]
    message = group_message["message"]

    try:
        # 搞个 r 占位, 因为 data 数据体不唯一
        r = 0
        dodoId = group_message["data"][r]["dodoId"]
        nickName = group_message["data"][r]["nickName"]
        level = group_message["data"][r]["level"]
        rank = group_message["data"][r]["rank"]
    except KeyError:
        print("\033[31m[Error]\033[0m 目标群可能未开通群等级")

    return group_message

# 获取群禁言名单信息
def getIslandMuteList(islandId, pageSize, maxId):
    URL = "https://botopen.imdodo.com/api/v1/island/mute/list"
    public_headers = Public_Headers.Headers

    # pageSize 最大值为100, maxId 为上一页最大ID值
    message_data = {
        "islandId": islandId,
        "pageSize": pageSize,
        "maxId": maxId
    }

    # 发送请求
    group_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))
    group_message = group_message.text
    group_message = json.loads(group_message)

    # 数据解析
    status = group_message["status"]
    message = group_message["message"]

    try:
        # 搞个 r 占位, 因为 data 数据体不唯一
        r = 0
        dodoId = group_message["data"]["maxId"]["list"][r]["dodoId"]

    except KeyError:
        print("\033[31m[Error]\033[0m 目标群可能没有被禁言人员")

    # 返回 json
    return group_message

# 获取群封禁名单信息
def getIslandBanList(islandId, pageSize, maxId):
    URL = "https://botopen.imdodo.com/api/v1/island/ban/list"
    public_headers = Public_Headers.Headers

    # pageSize 最大值为100, maxId 为上一页最大ID值
    message_data = {
        "islandId": islandId,
        "pageSize": pageSize,
        "maxId": maxId
    }

    # 发送请求
    group_message = requests.post(URL, headers=public_headers, data=json.dumps(message_data))
    group_message = group_message.text
    group_message = json.loads(group_message)

    # 数据解析
    status = group_message["status"]
    message = group_message["message"]

    try:
        # 搞个 r 占位, 因为 data 数据体不唯一
        r = 0
        dodoId = group_message["data"]["maxId"]["list"][r]["dodoId"]

    except KeyError:
        print("\033[31m[Error]\033[0m 目标群可能没有被封禁人员")

    # 返回 json
    return group_message


if __name__ == "__main__":
    islandId = 29118
    print(getIslandList())
    # print(getIslandInfo(islandId=islandId))
    # print(getIslandLevelRankList(islandId=islandId))
    # print(getIslandMuteList(islandId=islandId, pageSize=100, maxId=0))
    # print(getIslandBanList(islandId=islandId, pageSize=100, maxId=0))