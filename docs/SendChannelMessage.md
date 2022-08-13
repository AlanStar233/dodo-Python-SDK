### 十四、发送频道消息 SendChannelMessage

​	项目文件 -> [SendChannelMessage.py](../SendChannelMessage.py)

#### 14.1 send_text

##### 14.1.1 描述

​	发送文字消息

##### 14.1.2 用法

​	**传参**：channelId(频道ID)、messageType(消息类型)、content(内容)

> **注：content 支持 Markdown 格式。**
>
> **注：messageType  1: 文字信息  2: 图片信息  3: 视频信息**

​	**调用**：

```python
import SendChannelMessage

# 预定义, 或通过参数传递获得
channelId = 22222
messageType = 1
SendChannelMessage.send_text(channelId=channelId, messageType=messageType, content=content)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.2 send_pic

##### 14.2.1 描述

​	发送图片消息

##### 14.2.2 用法

​	**传参**：channelId(频道ID)、messageType(消息类型)、pic_url(图片地址)、width(图宽)、height(图高)

> **注：pic_url 必须为官方 URL 。**
>
> **注：messageType  1: 文字信息  2: 图片信息  3: 视频信息**

​	**调用**：

```python
import SendChannelMessage

# 预定义, 或通过参数传递获得
channelId = 22222
messageType = 1
pic_url = "https://xxx.xxx.xxx/xxx.jpg"
width = 200
height = 200
SendChannelMessage.send_pic(channelId=channelId, messageType=messageType, pic_url=pic_url, width=width, height=height)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.3 send_video

##### 14.3.1 描述

​	发送视频消息

##### 14.3.2 用法

​	**传参**：channelId(频道ID)、messageType(消息类型)、video_url(视频地址)、cover_url(封面地址)、duration(视频时间)、size(视频大小)

> **注：video_url 必须为官方 URL 。**
>
> **注：messageType  1: 文字信息  2: 图片信息  3: 视频信息**

​	**调用**：

```python
import SendChannelMessage

# 预定义, 或通过参数传递获得
channelId = 22222
messageType = 1
video_url = "https://xxx.xxx.xxx/xxx.mp4"
cover_url = "https://xxx.xxx.xxx/xxx.png"
SendChannelMessage.send_video(channelId=channelId, messageType=messageType, video_url=video_url, cover_url=cover_url, duration=100, size=100)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.4 edit

##### 14.4.1 描述

​	编辑文字内容

##### 14.4.2 用法

​	**传参**：channelId(频道ID)、messageType(消息类型)、content(修改后的内容)

> **注：因为当前只能编辑文字内容，所以messageType 为 1**
>
> **注：只能编辑机器人自己发出的内容。**
>
> **注：messageType  1: 文字信息  2: 图片信息  3: 视频信息**

​	**调用**：

```python
 import SendChannelMessage
 
# 预定义, 或通过参数传递获得
channelId = 22222
messageType = 1
content = "test"
SendChannelMessage.edit(channelId=channelId, messageType=messageType, content=content)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.5 withdraw

##### 14.5.1 描述

​	撤回消息

##### 14.5.2 用法

​	**传参**：messageId(消息ID)、reason(原因)

​	**调用**：

```python
 import SendChannelMessage
 
# 预定义, 或通过参数传递获得
messageId = 11111
reason = "test"
SendChannelMessage.withdraw(messageId=messageId, reason=reason)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.6 reaction_add

##### 14.6.1 描述

​	添加表情反应(贴表情)

##### 14.6.2 用法

​	**传参**：messageId(消息ID)、emoji_id(表情ID)

> **注：表情代码详见 -> [表情代码](https://open.imdodo.com/dev/api/message.html#%E6%B6%88%E6%81%AF%E8%A1%A8%E6%83%85)**

​	**调用**：

```python
 import SendChannelMessage
 
# 预定义, 或通过参数传递获得
messageId = 11111
emoji_id = 22222
SendChannelMessage.reaction_add(messageId=messageId, emoji_id=emoji_id)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |

#### 14.6 reaction_remove

##### 14.6.1 描述

​	移除表情反应

##### 14.6.2 用法

​	**传参**：messageId(消息ID)、emoji_id(表情ID)、dodoId(dodo号)

> **注：表情代码详见 -> [表情代码](https://open.imdodo.com/dev/api/message.html#%E6%B6%88%E6%81%AF%E8%A1%A8%E6%83%85)**
>
> **注：dodoId 不传或传空时则移除机器人自身 reaction**

​	**调用**：

```python
 import SendChannelMessage
 
# 预定义, 或通过参数传递获得
messageId = 11111
emoji_id = 22222
dodoId = 33333
SendChannelMessage.reaction_add(messageId=messageId, emoji_id=emoji_id, dodoId=dodoId)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述     |
| ------------ | ---- | -------- |
| message_info | dict | 操作信息 |