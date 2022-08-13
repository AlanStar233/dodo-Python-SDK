import json

import requests

import Public_Headers

# 获得群成员名单
def getMemberList(islandId, pageSize, maxId):
    URL = "https://botopen.imdodo.com/api/v1/member/list"
    public_headers = Public_Headers.Headers
    # pageSize 最大为 100
    memberData = {
        "islandId": str(islandId),
        "pageSize": pageSize,
        "maxId": maxId
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析, 但不放出
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 搞个 r 占位, 因为 list 中数据体不唯一
    r = 0
    # DODO号
    dodoId = member_info["data"]["list"][r]["dodoId"]
    # 群昵称
    nickName = member_info["data"]["list"][r]["nickName"]
    # 头像URL
    avatarUrl = member_info["data"]["list"][r]["avatarUrl"]
    # 加群时间
    joinTime = member_info["data"]["list"][r]["joinTime"]
    # 性别    -1: 保密  0: 女    1: 男
    sex = member_info["data"]["list"][r]["sex"]
    # 等级
    level = member_info["data"]["list"][r]["level"]
    # 是否为机器人    0: 否     1: 是
    isBot = member_info["data"]["list"][r]["isBot"]
    # 在线设备      0: 无    1: PC在线     2:手机在线
    onlineDevice = member_info["data"]["list"][r]["onlineDevice"]
    # 在线状态      0: 离线   1:在线    2:请勿打扰      3:离开
    onlineStatus = member_info["data"]["list"][r]["onlineStatus"]

    # 返回 json
    return member_info

# 获取成员信息
def getMemberInfo(islandId, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/member/info"
    public_headers = Public_Headers.Headers
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 群昵称
    nickName = member_info["data"]["nickName"]
    # DODO 昵称
    personalNickName = member_info["data"]["personalNickName"]
    # 头像URL
    avatarUrl = member_info["data"]["avatarUrl"]
    # 加群时间
    joinTime = member_info["data"]["joinTime"]
    # 性别    -1: 保密  0: 女    1: 男
    sex = member_info["data"]["sex"]
    # 等级
    level = member_info["data"]["level"]
    # 是否为机器人    0: 否     1: 是
    isBot = member_info["data"]["isBot"]
    # 在线设备      0: 无    1: PC在线     2:手机在线
    onlineDevice = member_info["data"]["onlineDevice"]
    # 在线状态      0: 离线   1:在线    2:请勿打扰      3:离开
    onlineStatus = member_info["data"]["onlineStatus"]

    # 返回 json
    return member_info

# 获取成员身份组列表
def getMemberRoleList(islandId, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/member/role/list"
    public_headers = Public_Headers.Headers
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析, 但不放出
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 搞个 r 占位, 因为 list 中数据体不唯一
    r = 0

    # 身份组ID
    roleId = member_info["data"][r]["roleId"]
    # 身份组名称
    roleName = member_info["data"][r]["roleName"]
    # 身份组颜色
    roleColor = member_info["data"][r]["roleColor"]
    # 身份组排序位置
    position = member_info["data"][r]["position"]
    # 身份组权限值 详见 -> https://open.imdodo.com/dev/start/permission.html#%E6%9D%83%E9%99%90%E5%80%BC%E8%AF%B4%E6%98%8E
    permission = member_info["data"][r]["permission"]

    # 返回 json
    return member_info

# 获取群邀请信息
def getInviteInfo(islandId, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/member/invitation/info"
    public_headers = Public_Headers.Headers
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    try:
        # 群昵称
        nickName = member_info["data"]["nickName"]
        # 邀请人数
        invitationCount = member_info["data"]["invitationCount"]
    except KeyError:
        print("\033[31m[Error]\033[0m 机器人可能权限不足, 需要提升至 超级管理员 级别")
    # 返回 json
    return member_info

# 编辑群成员昵称
def editMemberNickName(islandId, dodoId, nickName):
    URL = "https://botopen.imdodo.com/api/v1/member/nick/set"
    public_headers = Public_Headers.Headers
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
        "nickName": str(nickName)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 返回 json
    return member_info

# 禁言成员
def setMemberMute(islandId, dodoId, duration, reason):
    URL = "https://botopen.imdodo.com/api/v1/member/ban/set"
    public_headers = Public_Headers.Headers
    # duration 单位为秒
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
        "duration": duration,
        "reason": reason
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    return member_info

# 取消禁言成员
def removeMemberMute(islandId, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/member/mute/remove"
    public_headers = Public_Headers.Headers
    # duration 单位为秒
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    return member_info

# 永久封禁成员
def setBanForever(islandId, dodoId, noticeChannelId, reason):
    URL = "https://botopen.imdodo.com/api/v1/member/ban/add"
    public_headers = Public_Headers.Headers
    # duration 单位为秒
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
        "noticeChannelId": str(noticeChannelId),
        "reason": str(reason)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 返回 json
    return member_info

# 取消成员永久封禁
def removeBanForever(islandId, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/member/ban/remove"
    public_headers = Public_Headers.Headers
    # duration 单位为秒
    memberData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId)
    }

    # 发送请求及 json 格式化处理
    member_info = requests.post(URL, headers=public_headers, data=json.dumps(memberData))
    member_info = member_info.text
    member_info = json.loads(member_info)

    # 数据解析
    status = str(member_info["status"])
    status_message = member_info["message"]

    # 返回 json
    return member_info


if __name__ == "__main__":
    islandId = 29118
    dodoId = 254913173
    user_dodoId = 254923940
    maxId = 0
    noticeChannelId = 849618
    nickName = "Alan"
    reason = "测试一下禁言"
    # 获取成员列表
    # print(getMemberList(islandId=islandId, pageSize=100, maxId=maxId))
    # 获取成员信息
    # print(getMemberInfo(islandId=islandId, dodoId=dodoId))
    # 获取成员身份列表
    # print(getMemberRoleList(islandId=islandId, dodoId=dodoId))
    # 获取成员邀请信息, 仅超级管理员可查
    # print(getInviteInfo(islandId=islandId, dodoId=dodoId))
    # 编辑群成员昵称
    # TODO: 可能为bug, 机器人在其身份组, 能更改群主的昵称, 是否为需求? -> https://imdodo.com/p/345965355790999552
    # print(editMemberNickName(islandId=islandId, dodoId=dodoId, nickName=nickName))
    # 禁言成员
    # print(setMemberMute(islandId=islandId, dodoId=dodoId, duration=10, reason=reason))
    # 取消禁言成员
    # TODO: 有个点比较值得注意, 之前没有被禁言的用户, 执行取消禁言之后也是会请求成功的
    # print(removeMemberMute(islandId=islandId, dodoId=dodoId))
    # 永久封禁成员
    # print(setBanForever(islandId=islandId, dodoId=user_dodoId, noticeChannelId=noticeChannelId, reason=reason))
    # 取消永久封禁成员
    print(removeBanForever(islandId=islandId, dodoId=user_dodoId))