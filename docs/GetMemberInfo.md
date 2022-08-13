### 七、获取群成员信息 GetMemberInfo

​	项目文件 -> [GetMemberInfo.py](../GetMemberInfo)

#### 7.1 getMemberList()

##### 7.1.1 描述

​	获得群成员名单

##### 7.1.2 用法

​	**传参**：islandId(群号)、pageSize(页大小, 最大为100)、maxId(上一页最大ID)

​	**调用**：

```python
import GetMemberInfo

# 预定义, 或通过参数传递获得
islandId = 23333
pageSize = 20
maxId = 0
GetMemberInfo.getMemberList(islandId=islandId, pageSize=pageSize, maxId=maxId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述       |
| ----------- | ---- | ---------- |
| member_info | dict | 群成员名单 |

#### 7.2 getMemberInfo()

##### 7.2.1 描述

​	获得群成员信息

##### 7.2.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)

​	**调用**：

```python
import GetMemberInfo

# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
GetMemberInfo.getMemberInfo(islandId=islandId, dodoId=dodoId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述       |
| ----------- | ---- | ---------- |
| member_info | dict | 群成员信息 |

#### 7.3 getMemberRoleList()

##### 7.3.1 描述

​	获得群成员身份信息

##### 7.3.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)

​	**调用**：

```python
import GetMemberInfo

# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
GetMemberInfo.getMemberRoleList(islandId=islandId, dodoId=dodoId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述           |
| ----------- | ---- | -------------- |
| member_info | dict | 群成员身份信息 |

#### 7.4 getInviteInfo()

##### 7.4.1 描述

​	获得群邀请名单

##### 7.4.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)

​	**调用**：

```python
import GetMemberInfo

# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
GetMemberInfo.getInviteInfo(islandId=islandId, dodoId=dodoId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述       |
| ----------- | ---- | ---------- |
| member_info | dict | 群邀请名单 |

#### 7.5 editMemberNickName()

##### 7.5.1 描述

​	编辑群成员昵称

##### 7.5.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)、nickName(新昵称)

​	**调用**：

```python
import GetMemberInfo

# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
nickName = "乆乆乆"
GetMemberInfo.editMemberNickName(islandId=islandId, dodoId=dodoId, nickName=nickName)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述     |
| ----------- | ---- | -------- |
| member_info | dict | 执行结果 |

#### 7.6 setMemberMute()

##### 7.6.1 描述

​	禁言群成员

##### 7.6.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)、duration(时间，单位为秒，最长7天)、reason(原因)

​	**调用**：

```python
 import GetMemberInfo
 
# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
duration = 10
reason = "禁言测试~"
GetMemberInfo.setMemberMute(islandId=islandId, dodoId=dodoId, duration=duration, reason=reason)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述     |
| ----------- | ---- | -------- |
| member_info | dict | 执行结果 |

#### 7.7 removeMemberMute()

##### 7.7.1 描述

​	取消禁言群成员

##### 7.7.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)

​	**调用**：

```python
 import GetMemberInfo
 
# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
GetMemberInfo.removeMemberMute(islandId=islandId, dodoId=dodoId, duration=duration, reason=reason)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述     |
| ----------- | ---- | -------- |
| member_info | dict | 执行结果 |

#### 7.8 setBanForever()

##### 7.8.1 描述

​	封禁群成员

##### 7.8.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)、noticeChannelId(封禁消息通知所在频道ID)、reason(原因)

​	**调用**：

```python
import GetMemberInfo
  
# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
noticeChannelId = 22222
reason = "禁言测试~"
GetMemberInfo.setBanForever(islandId=islandId, dodoId=dodoId, noticeChannelId=noticeChannelId, reason=reason)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述     |
| ----------- | ---- | -------- |
| member_info | dict | 执行结果 |

#### 7.9 removeBanForever()

##### 7.9.1 描述

​	取消封禁群成员

##### 7.9.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)

​	**调用**：

```python
import GetMemberInfo
  
# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
GetMemberInfo.removeBanForever(islandId=islandId, dodoId=dodoId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述     |
| ----------- | ---- | -------- |
| member_info | dict | 执行结果 |

