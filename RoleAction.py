import json

import requests

import Public_Headers

# 获取身份组列表
def getRoleList(islandId):
    URL = "https://botopen.imdodo.com/api/v1/role/list"
    public_headers = Public_Headers.Headers
    roleData = {
        "islandId": str(islandId)
    }

    # 发送请求及 json 格式化处理
    role_info = requests.post(URL, headers=public_headers, data=json.dumps(roleData))
    role_info = role_info.text
    role_info = json.loads(role_info)

    # 数据解析, 但不放出来
    status = str(role_info["status"])
    status_message = role_info["message"]

    # 搞个 r 占位, 因为 data 数据体不唯一
    r = 0
    # 身份组ID
    roleId = role_info["data"][r]["roleId"]
    # 身份组名称
    roleName = role_info["data"][r]["roleName"]
    # 身份组颜色
    roleColor = role_info["data"][r]["roleColor"]
    # 身份组排序位
    position = role_info["data"][r]["position"]
    # 身份组权限值 详见 -> https://open.imdodo.com/dev/start/permission.html#%E6%9D%83%E9%99%90%E5%80%BC%E8%AF%B4%E6%98%8E
    permission = role_info["data"][r]["permission"]

    # 返回 json
    return role_info

# 赋予成员身份组
def setRole(islandId, dodoId, roleId):
    URL = "https://botopen.imdodo.com/api/v1/role/member/add"
    public_headers = Public_Headers.Headers
    roleData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
        "roleId": str(roleId)
    }

    # 发送请求及 json 格式化处理
    role_info = requests.post(URL, headers=public_headers, data=json.dumps(roleData))
    role_info = role_info.text
    role_info = json.loads(role_info)

    # 数据解析
    status = str(role_info["status"])
    status_message = role_info["message"]

    # 返回 json
    return role_info

# 移除成员身份组
def removeRole(islandId, dodoId, roleId):
    URL = "https://botopen.imdodo.com/api/v1/role/member/remove"
    public_headers = Public_Headers.Headers
    roleData = {
        "islandId": str(islandId),
        "dodoId": str(dodoId),
        "roleId": str(roleId)
    }

    # 发送请求及 json 格式化处理
    role_info = requests.post(URL, headers=public_headers, data=json.dumps(roleData))
    role_info = role_info.text
    role_info = json.loads(role_info)

    # 数据解析
    status = str(role_info["status"])
    status_message = role_info["message"]

    # 返回 json
    return role_info


if __name__ == "__main__":
    islandId = 29118
    dodoId = 254913173
    roleId = 111927  # 实习版主
    # 获取群内身份组列表
    # print(getRoleList(islandID=islandId))
    # 赋予成员身份组
    # print(setRole(islandId=islandId, dodoId=dodoId, roleId=roleId))
    # 移除成员身份组
    print(removeRole(islandId=islandId, dodoId=dodoId, roleId=roleId))