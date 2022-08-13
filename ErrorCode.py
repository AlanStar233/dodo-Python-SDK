import json

# 将传递来的状态码转化为对应消息返回 -> ./res/error_code.json
# status_code 需要为字符串
def dodo_code(status_code):
    with open("res/error_code.json", mode="r", encoding="UTF-8") as doc:
        dodo_doc = doc.read()
    dodo_doc = json.loads(dodo_doc)
    message = dodo_doc[status_code]
    return message
