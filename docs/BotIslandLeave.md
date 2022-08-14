### 二、机器人退群行为 BotIslandLeave

​	项目文件 -> [BotIslandLeave.py](../BotIslandLeave.py)

#### 2.1 leave()

##### 2.1.1 描述

​	机器人退群。

##### 2.1.2 用法

​	**传参**：islandId(群号)

​	**调用**：

```python
import BotsIslandLeave

# 需要预先获取或自定义 islandId
islandId = 111111
BotsIslandLeave.leave(islandId=islandId)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述               |
| ------------- | ---- | ------------------ |
| leave_message | dict | 退群是否成功的信息 |