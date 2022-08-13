import json
import requests
import Public_Headers
import MarkdownSupport

# TODO: 频道消息支持Markdown
# 官方文档要求入参 referencedMessageId, 但无用法
# messageType  1: 文字信息  2: 图片信息  3: 视频信息

# 文字消息
def send_text(channelId, messageType, content):
    # 预定义 URL 和 公共头
    URL = "https://botopen.imdodo.com/api/v1/channel/message/send"
    public_headers = Public_Headers.Headers
    textData = {
        "channelId": channelId,
        "messageType": messageType,
        "messageBody": {
            "content": content
        }
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    # 信息ID
    messageId = message_info["data"]["messageId"]

    # 打印信息ID
    print("\033[92m[Info]\033[0m 信息已发送", messageId)

    # 返回 json
    return message_info

# 图片消息
def send_pic(channelId, messageType, pic_url, width, height):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/send"
    public_headers = Public_Headers.Headers
    textData = {
        "channelId": channelId,
        "messageType": messageType,
        "messageBody": {
            "url": pic_url,
            "width": width,
            "height": height,
            "isOriginal": 1
        }
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    # 信息ID
    messageId = message_info["data"]["messageId"]

    # 打印信息ID
    print("\033[92m[Info]\033[0m 信息已发送", messageId)

    # 返回 json
    return message_info

# 视频消息
def send_video(channelId, messageType, video_url, cover_url, duration, size):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/send"
    public_headers = Public_Headers.Headers
    textData = {
        "channelId": channelId,
        "messageType": messageType,
        "messageBody": {
            "url": video_url,
            "coverUrl": cover_url,
            "duration": duration,
            "size": size
        }
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    # 信息ID
    messageId = message_info["data"]["messageId"]

    # 打印信息ID
    print("\033[92m[Info]\033[0m 信息已发送", messageId)

    # 返回 json
    return message_info

# 编辑信息  当前只能编辑文字内容, 所以messageType 为 1
def edit(messageId, messageType, content):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/edit"
    public_headers = Public_Headers.Headers
    textData = {
        "messageId": messageId,
        "messageType": messageType,
        "messageBody": {
            "content": content
        }
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    # 若更改了非机器人发出的消息, 会报10051 code
    if status != "10051":
        return message_info
    else:
        print("\033[31m[Error]\033[0m ", "仅可编辑机器人自己发送的消息")
        return message_info

# 撤回消息
def withdraw(messageId, reason):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/withdraw"
    public_headers = Public_Headers.Headers
    textData = {
        "messageId": messageId,
        "reason": reason
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    return message_info

# 添加表情反应
def reaction_add(messageId, emoji_id):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/reaction/add"
    public_headers = Public_Headers.Headers
    # TODO: 表情类型, type 取 1
    # 表情代码详见 -> https://open.imdodo.com/dev/api/message.html#%E6%B6%88%E6%81%AF%E8%A1%A8%E6%83%85
    textData = {
        "messageId": messageId,
        "emoji": {
            "type": 1,
            "id": str(emoji_id)
        }
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    return message_info

def reaction_remove(messageId, emoji_id, dodoId):
    URL = "https://botopen.imdodo.com/api/v1/channel/message/reaction/remove"
    public_headers = Public_Headers.Headers
    # TODO: 表情类型, type 取 1
    # TODO: dodoId 不传或传空时则移除机器人自身反应
    # 表情代码详见 -> https://open.imdodo.com/dev/api/message.html#%E6%B6%88%E6%81%AF%E8%A1%A8%E6%83%85
    textData = {
        "messageId": messageId,
        "emoji": {
            "type": 1,
            "id": str(emoji_id)
        },
        "dodoId": str(dodoId)
    }

    # 发送请求及 json 格式化处理
    message_info = requests.post(URL, headers=public_headers, data=json.dumps(textData))
    message_info = message_info.text
    message_info = json.loads(message_info)

    # 数据解析
    status = str(message_info["status"])
    status_message = message_info["message"]

    return message_info


if __name__ == "__main__":
    textMessage = MarkdownSupport.anti_spoilers(MarkdownSupport.bold("你好你好~"))
    pic_url = "https://img.imdodo.com/dodo/8c77d48865bf547a69fb3bba6228760c.png"
    video_url = "https://video.imdodo.com/dodo/ff85c752daf7d67884cb9ad3921a5d01.mp4"
    video_cover = "https://img.imdodo.com/dodo/8c77d48865bf547a69fb3bba6228760c.png"
    messageType_text = 1
    messageType_pic = 2
    messageType_video = 3
    channelId = 849618

    messageId = 345612360456810496
    edit_content = MarkdownSupport.anti_spoilers(MarkdownSupport.bold("才不是要被改呢!"))
    reason = "只是想单纯做个测试而已啦~"
    emoji_id = 128516
    dodoId = ""
    # 发文字
    # print(send_text(channelId=channelId, messageType=messageType_text, content=textMessage))
    # 发图片
    # print(send_pic(channelId=channelId, messageType=messageType_pic, pic_url=pic_url, width=500, height=500))
    # 发视频
    # print(send_video(channelId=channelId, messageType=messageType_video, video_url=video_url, cover_url=video_cover,
    #            duration=100, size=100))
    # 编辑消息
    # print(edit(messageId=messageId, messageType=1, content=edit_content))
    # 撤回消息
    # print(withdraw(messageId=messageId, reason=reason))
    # 贴表情测试
    # print(reaction_add(messageId=messageId, emoji_id=emoji_id))
    # 取消贴表情测试
    print(reaction_remove(messageId=messageId, emoji_id=emoji_id, dodoId=dodoId))