# 粗体
def bold(message):
    message = "**" + message + "**"
    return message

# 斜体
def italic(message):
    message = "*" + message + "*"
    return message

# 底线
def baseline(message):
    message = "__" + message + "__"
    return message

# 链接
def link(desc, url):
    message = "[" + desc + "]" + "(" + url + ")"
    return message

# 删除线
def delLine(message):
    message = "~~" + message + "~~"
    return message

# 防剧透
def anti_spoilers(message):
    message = "||" + message + "||"
    return message

# 引用
def quote(message):
    message = ">" + message
    return message

# 代码块
def code_block(message):
    message = "```" + message + "```"
    return message

# 菱形语法
# 艾特用户
def at_user(dodoId):
    message = "<@!" + dodoId + ">"
    return message

# 跳转频道
def jump_channel(channelId):
    message = "<#" + channelId + ">"
    return message


if __name__ == "__main__":
    __my_message = "你好"
    __desc = "哔哩哔哩"
    __url = "https://www.bilibili.com"
    __code = "print('hello world')"
    __dodoId = "254913173"
    __channel_Id = "850273"
    print("粗体", bold(__my_message))
    print("斜体", italic(__my_message))
    print("粗体&斜体", bold(italic(__my_message)))
    print("链接", link(__desc, __url))
    print("删除线", delLine(__my_message))
    print("防剧透", anti_spoilers(__my_message))
    print("引用", quote(__my_message))
    print("代码块", code_block(__code))
    print("艾特用户", at_user(__dodoId))
    print("跳转频道", jump_channel(__channel_Id))
