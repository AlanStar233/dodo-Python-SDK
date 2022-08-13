### 一、机器人信息 BotInfo

​	项目文件 -> [BotInfo.py](../BotInfo.py)

#### 1.1 config_status()

##### 1.1.1 描述

​	用于对 [./config/bot_Info.json](../config/bot_Info.json)， 即 **机器人配置文件**的检测。配置文件中存放 dodo 开放平台提供给机器人的 **clientId** 和 **token**。

​	**所有操作**都需要依赖这两个参数进行。

##### 1.1.2 用法

​	**传参**：不需要传参

​	**调用**：

```python
import BotInfo
BotInfo.config_status()
```

​	**返回结果**：

| 返回参数 | 类型 | 描述                                                 |
| -------- | ---- | ---------------------------------------------------- |
| type     | int  | 当 clientId 或 token 为空时将返回 -1，其余情况返回 0 |

#### 1.2 get_ClientId()

##### 1.2.1 描述

​	读取 [../config/bot_Info.json](../config/bot_Info.json) 中的 clientId，并返回。

##### 1.2.2 用法

​	**传参**：不需要传参

​	**调用**：

```python
import BotInfo
BotInfo.get_clientId()
```

​	**返回结果**：

| 返回参数 | 类型 | 描述                    |
| -------- | ---- | ----------------------- |
| clientId | str  | 开放平台提供的 clientId |

#### 1.3 get_token()

##### 1.3.1 描述

​	读取 [../config/bot_Info.json](../config/bot_Info.json) 中的 token，并返回。

##### 1.3.2 用法

​	**传参**：不需要传参

​	**调用**：

```python
import BotInfo
BotInfo.get_token()
```

​	**返回结果**：

| 返回参数 | 类型 | 描述                 |
| -------- | ---- | -------------------- |
| token    | str  | 开放平台提供的 token |

#### 1.4 combine_Authorization()

##### 1.4.1 描述

​	拼接 clientId 和 token 组合成[公共请求头](../Public_Headers.py)中的 **Authorization** 参数。

##### 1.4.2 用法

​	**传参**：不需要传参

​	**调用**：

```
import BotInfo
BotInfo.combine_Authorization()
```

​	**返回结果**:

| 返回参数      | 类型 | 描述                                  |
| ------------- | ---- | ------------------------------------- |
| Authorization | str  | 根据 clientId 和 token 拼接的鉴权参数 |

