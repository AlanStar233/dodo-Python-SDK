<p align="center">
  <a href="https://open.imdodo.com">
    <img src="https://open.imdodo.com/favicon.png" width="200" height="200" alt="dodo-open">
  </a>
</p>

<div align="center">

  # dodo-Python-SDK

</div>

<div align="center">

  ### 一个希望所有人都能轻松上手的 SDK

</div>

<div align="center">
    <a href="https://github.com/AlanStar233/dodo-Python-SDK/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/AlanStar233/dodo-Python-SDK?style=social"></a>
	<a href="https://github.com/AlanStar233/dodo-Python-SDK/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/AlanStar233/dodo-Python-SDK?style=social"></a>
	<a href="https://github.com/AlanStar233/dodo-Python-SDK/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/AlanStar233/dodo-Python-SDK?style=social"></a>
</div>

> 提醒：由于个人原因<s>(绝赞网课中)</s>, 本项目可能会放缓与开放平台的更新同步, 但基础功能不影响使用, 如有好心人可发起PR。

<details>
<summary>更新日志</summary>

### 2022-08-23

基于开放平台更新 0.1.3 已完成新增接口接入

- 新增 频道API-创建频道 (于[GetChannelInfo.py](./GetChannelInfo.py))
- 新增 频道API-编辑频道 (于[GetChannelInfo.py](./GetChannelInfo.py))
- 新增 频道API-删除频道 (于[GetChannelInfo.py](./GetChannelInfo.py))
- 完善 文字频道API-发送消息，新增消息类型卡片消息，新增DoDo号字段 (于[GetChannelInfo.py](./GetChannelInfo.py))
- (开发中) 完善 文字频道API-编辑消息，新增消息类型卡片消息，新增DoDo号字段 (于[GetChannelInfo.py](./GetChannelInfo.py))
- 新增 身份组API-创建身份组 (于[RoleAction.py](./RoleAction.py))
- 新增 身份组API-编辑身份组 (于[RoleAction.py](./RoleAction.py))
- 新增 身份组API-删除身份组 (于[RoleAction.py](./RoleAction.py))
</details>

## 项目简介

​	本项目基于 [**DoDo开放平台-内测平台**](https://open.imdodo.com) 提供的API接口进行再封装，提供了目前开放平台提供的所有接口能力。

## 开源协议

​	本项目采用 [**MIT-Licenses**](https://choosealicense.com/licenses/mit/) 作为开源协议。

## 开发工具

​	PyCharm Professional Early Access Program

## 项目详解

​	接下来，我将以**文件**为单位，逐一解释其中提供的方法。

​	由于文件过多，这里只提供对应**项目文件**和**解释文件**的地址。

### 一、机器人信息 BotInfo

​	项目文件 -> [BotInfo.py](./BotInfo.py)

​	解释文件 -> [BotInfo.md](./docs/BotInfo.md)

### 二、机器人退群行为 BotIslandLeave

​	项目文件 -> [BotIslandLeave.py](./BotIslandLeave.py)

​	解释文件 -> [BotIslandLeave.md](./docs/BotIslandLeave.md)

### 三、资源上传 DoResourceUpload

​	项目文件 -> [DoResourceUpload.py](./DoResourceUpload.py)

​	解释文件 -> [DoResourceUpload.md](./docs/DoResourceUpload.md)

### 四、错误码 ErrorCode

​	项目文件 -> [ErrorCode.py](./ErrorCode.py)

​	解释文件 -> [ErrorCode.md](./docs/ErrorCode.md)

### 五、获取频道信息 GetChannelInfo

​	项目文件 -> [GetChannelInfo.py](./GetChannelInfo.py)

​	解释文件 -> [GetChannelInfo.md](./docs/GetChannelInfo.md)

### 六、获取群信息 GetGroupInfo

​	项目文件 -> [GetGroupInfo.py](./GetGroupInfo.py)

​	解释文件 -> [GetGroupInfo.md](./docs/GetGroupInfo.md)

### 七、获取群成员信息 GetMemberInfo

​	项目文件 -> [GetMemberInfo.py](./GetMemberInfo.py)

​	解释文件 -> [GetMemberInfo.md](./docs/GetMemberInfo.md)

### 八、获取群成员NFT

​	项目文件 -> [GetMemberNFT.py](./GetMemberNFT.py)

​	解释文件 -> [GetMemberNFT.md](./docs/GetMemberNFT.md)

### 九、获取 WebSocket 地址 GetWebSocketConnection

​	项目文件 -> [GetWebSocketConnection.py](./GetWebSocketConnection.py)

​	解释文件 -> [GetWebSocketConnection.md](./docs/GetWebSocketConnection.md)

### 十、log依赖 Loghelper

​	项目文件 -> [Loghelper.py](./Loghelper.py)

​	解释文件 -> <u>没有开放接口故不做解释</u>

### 十一、dodo Markdown 支持 MarkdownSupport

​	项目文件 -> [MarkdownSupport.py](./MarkdownSupport.py)

​	解释文件 -> [MarkdownSupport.md](./docs/MarkdownSupport.md)

### 十二、公共请求头 Public_Headers

​	项目文件 -> [Public_Headers.py](./Public_Headers.py)

​	解释文件 -> [Public_Headers.md](./docs/Public_Headers.md)

### 十三、身份行为 RoleAction

​	项目文件 -> [RoleAction.py](./RoleAction.py)

​	解释文件 -> [RoleAction.md](./docs/RoleAction.md)

### 十四、发送频道消息 SendChannelMessage

​	项目文件 -> [SendChannelMessage.py](./SendChannelMessage.py)

​	解释文件 -> [SendChannelMessage.md](./docs/SendChannelMessage.md)

### 十五、发送私信 SendPersonalMessage

​	项目文件 -> [SendPersonalMessage.py](./SendPersonalMessage.py)

​	解释文件 -> [SendPersonalMessage.md](./docs/SendPersonalMessage.md)

### 十六、WebSocket 通信 WebSocketConnection	

​	项目文件 -> [WebSocketConnection.py](./WebSocketConnection.py)

​	解释文件 -> [WebSocketConnection.md](./docs/WebSocketConnection.md)

------

### 十七、demo

​	根据当前 SDK 做了个示例项目，不定期更新，点个 star 吧旁友们 orz

​	↓↓↓

​	[dodo-demo-Project](https://github.com/AlanStar233/dodo-demo-Project)
