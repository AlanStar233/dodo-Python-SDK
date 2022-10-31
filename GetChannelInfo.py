#  @Author:     AlanStar
#  @Contact:    alan233@vip.qq.com
#  @License:    MIT
#  Copyright (c) 2022-2022

import requests
import json
import Public_Headers

# 获取频道列表
def getChannelList(islandId):
    URL = "https://botopen.imdodo.com/api/v1/channel/list"
    public_headers = Public_Headers.Headers
    data = {
        "islandId": islandId
    }

    # 发送请求
    channelData = requests.post(URL, headers=public_headers, data=json.dumps(data))  # 这里需要dumps
    channelData = channelData.text
    channelData = json.loads(channelData)

    # 数据解析, 但不发出，可改
    r = 0  # 初始值

    # 频道ID
    channelId = channelData["data"][r]["channelId"]
    # 频道名称
    channelName = channelData["data"][r]["channelName"]
    # 默认访问频道标识  0: 否  1:是
    defaultFlag = channelData["data"][r]["defaultFlag"]
    # 频道类型        1:文字频道   2:语音频道  4:帖子频道  5:链接频道  6:资料频道
    channelType = channelData["data"][r]["channelType"]
    # 分组ID
    groupId = channelData["data"][r]["groupId"]
    # 分组名称
    groupName = channelData["data"][r]["groupName"]

    # 这里只返回json数据
    return channelData

# 获取频道信息
def getChannelInfo(channelId):
    URL = "https://botopen.imdodo.com/api/v1/channel/info"
    public_headers = Public_Headers.Headers
    data = {
        "channelId": channelId
    }

    # 发送请求
    channelInfoData = requests.post(URL, headers=public_headers, data=json.dumps(data))
    channelInfoData = channelInfoData.text
    channelInfoData = json.loads(channelInfoData)

    # 数据解析, 但不发出，可改
    status = channelInfoData["status"]
    message = channelInfoData["message"]

    # 频道名称
    channelName = channelInfoData["data"]["channelName"]
    # 频道类型        1:文字频道   2:语音频道  4:帖子频道  5:链接频道  6:资料频道
    channelType = channelInfoData["data"]["channelType"]
    # 群号
    islandId = channelInfoData["data"]["islandId"]
    # 默认访问频道标识  0: 否  1:是
    defaultFlag = channelInfoData["data"]["defaultFlag"]
    # 分组ID
    groupId = channelInfoData["data"]["groupId"]
    # 分组名称
    groupName = channelInfoData["data"]["groupName"]

    # 这里只返回json数据
    return channelInfoData

# 创建频道
def createChannel(islandId, channelName, channelType):
    URL = "https://botopen.imdodo.com/api/v1/channel/add"
    public_headers = Public_Headers.Headers
    data = {
        "islandId": islandId,
        "channelName": channelName,
        # 1：文字频道，2：语音频道（默认自由模式），4：帖子频道（默认详细模式）出参
        "channelType": channelType
    }

    # 发送请求
    channelData = requests.post(URL, headers=public_headers, data=json.dumps(data))  # 这里需要dumps
    channelData = channelData.text
    channelData = json.loads(channelData)

    # 数据解析, 不发出
    # 状态
    status = channelData["status"]
    message = channelData["message"]
    channelId = channelData["data"]["channelId"]

    # 这里只返回 json 数据
    return channelData

# 编辑频道
def editChannel(islandId, channelId, channelName):
    URL = "https://botopen.imdodo.com/api/v1/channel/edit"
    public_headers = Public_Headers.Headers
    data = {
        "islandId": islandId,
        # 频道名称可为空
        "channelName": channelName,
        "channelId": channelId
    }

    # 发送请求
    channelData = requests.post(URL, headers=public_headers, data=json.dumps(data))  # 这里需要dumps
    channelData = channelData.text
    channelData = json.loads(channelData)

    # 数据解析, 不发出
    # 状态
    status = channelData["status"]
    message = channelData["message"]

    # 这里只返回 json 数据
    return channelData

# 删除频道
def removeChannel(islandId, channelId):
    URL = "https://botopen.imdodo.com/api/v1/channel/remove"
    public_headers = Public_Headers.Headers
    data = {
        "islandId": islandId,
        "channelId": channelId
    }

    # 发送请求
    channelData = requests.post(URL, headers=public_headers, data=json.dumps(data))  # 这里需要dumps
    channelData = channelData.text
    channelData = json.loads(channelData)

    # 数据解析, 不发出
    # 状态
    status = channelData["status"]
    message = channelData["message"]

    # 这里只返回 json 信息
    return channelData


if __name__ == "__main__":
    islandId = 29118
    # channelName = "只是个平平无奇的测试频道罢了"
    # channelName = "只是个平平无奇的测试频道"
    channelType = 1
    channelId = 1059987
    # channelData = getChannelList(islandId=islandId)
    # print(channelData)
    # print(createChannel(islandId=islandId, channelName=channelName, channelType=channelType))
    # print(editChannel(islandId=islandId, channelId=channelId, channelName=channelName))
    print(removeChannel(islandId=islandId, channelId=channelId))