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


if __name__ == "__main__":
    islandId = 29118
    channelData = getChannelList(islandId=islandId)
    print(channelData)
