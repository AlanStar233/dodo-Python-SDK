import json
from requests import Request, Session
from urllib3 import encode_multipart_formdata
import BotInfo

def pic_upload(filePath, fileName):
    URL = "https://botopen.imdodo.com/api/v1/resource/picture/upload"
    # 重新指定请求头, 此处不使用 PublicHeaders.py
    file_data = {
        "file": (fileName, open(filePath, "rb").read())
    }
    # 编码 multipart-data
    encode_data = encode_multipart_formdata(file_data)
    data = encode_data[0]
    # 重构请求头
    public_headers = {
        "Content-Type": encode_data[1],
        "Authorization": BotInfo.combine_Authorization()
    }
    # 调试用
    # print(public_headers)
    # print(filePath)

    # 生成请求体, 通过 session 请求,
    s = Session()
    req = Request("POST", url=URL, headers=public_headers, data=data)
    # 预计算请求头中的 Content-Length
    prepped = req.prepare()
    # 调试用
    # print(prepped.headers)
    # 使用 session 发送请求
    file_message = s.send(prepped)

    # 接受返回信息并转为 json
    file_message = file_message.text
    file_message = json.loads(file_message)

    # 数据解析
    print(file_message)
    status = file_message["status"]
    message = file_message["message"]

    # 返回 json
    return file_message


if __name__ == "__main__":
    filePath = "C:\\Users\\AlanStar\\Desktop\\B站头像.jpg"
    # fileSize = 369017
    # fileName 可以指定, 起什么名字都可以
    fileName = "pic.jpg"
    pic_upload(filePath=filePath, fileName=fileName)
