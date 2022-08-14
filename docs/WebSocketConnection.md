### 十六、WebSocket 通信 WebSocketConnection	

​	项目文件 -> [WebSocketConnection.py](../WebSocketConnection.py)

#### 16.1 on_message()

##### 16.1.1 描述

​	WebSocket 接收到信息做出的反应。

##### 16.1.2 用法

​	消息体解析已在项目文件中写出，可自行参照其他文档的参数编写逻辑使用。

> **注：项目文件给出了message接口，可在on_message()方法中根据传回来的 json 解析出 messageType 从而分辨出不同的 Event**
>
> **注：有关 Event 可查看官方文档 -> [消息 Event](https://open.imdodo.com/dev/event/channel-text.html)**

#### 16.2 on_error()

##### 16.2.1 描述

​	WebSocket 接收到错误时做出的反应。

##### 16.2.2 用法

​	一般不需要更改，保持原样即可。

#### 16.3 on_close()

##### 16.3.1 描述

​	WebSocket 连接关闭做出的反应。

##### 16.3.2 用法

​	一般不需要更改，保持原样即可。

#### 16.4 on_open()

##### 16.4.1 描述

​	WebSocket 信道创建时做出的反应。

##### 16.4.2 用法

​	一般不需要更改，保持原样即可。

#### 16.5 on_ping()

##### 16.5.1 描述

​	WebSocket 维持长连接发出心跳包。

##### 16.5.2 用法

​	一般不需要更改，保持原样即可。

#### 16.6 on_pong()

##### 16.6.1 描述

​	WebSocket 维持长连接接收到服务器的响应。

##### 16.6.2 用法

​	一般不需要更改，保持原样即可。