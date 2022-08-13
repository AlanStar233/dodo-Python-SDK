### 十五、发送私信 SendPersonalMessage

​	项目文件 -> [SendPersonalMessage.py](../SendPersonalMessage.py)

#### 15.1 send()

##### 15.1.1 描述

​	发送私信

##### 15.1.2 用法

​	**传参**：dodoId(dodo号)、messageType(消息类型)、content(内容)

> **注：私信消息不支持 Markdown**

​	**调用**：

```python
import SendPersonalMessage

# 预定义, 或通过参数传递获得
dodoId = 11111
messageType = 1
content = "test"
SendPersonalMessage.send(dodoId=dodoId, messageType=messageType, content=content)
```

​	**返回结果**：

| 返回参数 | 类型 | 描述 |
| -------- | ---- | ---- |
| -        | -    | -    |

> **注：这里会直接 print 操作结果，可自行加上 return**