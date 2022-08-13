### 六、获取群信息 GetGroupInfo

​	项目文件 -> [GetGroupInfo.py](../GetGroupInfo.py)

#### 6.1 getIslandList()

##### 6.1.1 描述

​	获取群列表

##### 6.1.2 用法

​	**传参**：不需要传参

​	**调用**：

```python
import GetGroupInfo

GetGroupInfo.getIslandList()
```

​	**返回结果**：

| 返回参数      | 类型 | 描述       |
| ------------- | ---- | ---------- |
| group_message | dict | 群列表信息 |

#### 6.2 getIslandInfo()

##### 6.2.1 描述

​	获取群信息

##### 6.2.2 用法

​	**传参**：islandId(群ID)

​	**调用**：

```python
import GetGroupInfo

# 预定义群ID, 或通过参数传递获得
islandId = 23333
GetGroupInfo.getIslandInfo(islandId=islandId)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述   |
| ------------- | ---- | ------ |
| group_message | dict | 群信息 |

#### 6.3 getIslandLevelRankList()

##### 6.3.1 描述

​	获取群等级信息

##### 6.3.2 用法

​	**传参**：islandId(群ID)

​	**调用**：

```python
import GetGroupInfo

# 预定义群ID, 或通过参数传递获得
islandId = 23333
GetGroupInfo.getIslandLevelRankList(islandId=islandId)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述       |
| ------------- | ---- | ---------- |
| group_message | dict | 群等级信息 |

#### 6.4 getIslandMuteList()

##### 6.4.1 描述

​	获取群禁言名单信息

##### 6.4.2 用法

​	**传参**：islandId(群ID)、pageSize(页大小，最大值为100)、maxId(上一页最大ID)

​	**调用**：

```python
import GetGroupInfo

# 预定义, 或通过参数传递获得
islandId = 23333
pageSize = 20
maxId = 0
GetGroupInfo.getIslandMuteList(islandId=islandId, pageSize=pageSize, maxId=maxId)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述           |
| ------------- | ---- | -------------- |
| group_message | dict | 群禁言名单信息 |

#### 6.5 getIslandBanList()

##### 6.5.1 描述

​	获取群封禁名单信息

##### 6.5.2 用法

​	**传参**：islandId(群ID)、pageSize(页大小，最大值为100)、maxId(上一页最大ID)

​	**调用**：

```python
import GetGroupInfo

# 预定义, 或通过参数传递获得
islandId = 23333
pageSize = 20
maxId = 0
GetGroupInfo.getIslandBanList(islandId=islandId, pageSize=pageSize, maxId=maxId)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述           |
| ------------- | ---- | -------------- |
| group_message | dict | 群封禁名单信息 |

