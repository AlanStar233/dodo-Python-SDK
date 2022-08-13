### 五、获取频道信息 GetChannelInfo

​	项目文件 -> [GetChannelInfo.py](../GetChannelInfo.py)

#### 5.1 getChannelList()

##### 5.1.1 描述

​	获取频道列表

##### 5.1.2 用法

​	**传参**：islandId(群ID)

​	**调用**：

```python
import GetChannelInfo

# 定义群ID
islandId = 23333
GetChannelInfo.getChannelList(islandId=islandId)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述         |
| ----------- | ---- | ------------ |
| channelData | dict | 频道列表数据 |

#### 5.2 getChannelList()

##### 5.2.1 描述

​	获取频道信息

##### 5.2.2 用法

​	**传参**：channelId(频道ID)

​	**调用**：

```python
import GetChannelInfo

# 定义群ID
channelId = 23333
GetChannelInfo.getChannelInfo(channelId=channelId)
```

​	**返回结果**：

| 返回参数        | 类型 | 描述     |
| --------------- | ---- | -------- |
| channelInfoData | dict | 频道数据 |