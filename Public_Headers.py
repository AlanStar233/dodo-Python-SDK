import BotInfo
from urllib3 import encode_multipart_formdata
# 公共请求头, 机器人的每次对API的请求都需要添加
Headers = {
    "Content-Type": "application/json",
    "Authorization": BotInfo.combine_Authorization()
}

def getUploadHeaders(fileName, filePath):
    file_data = {
        "file": (fileName, open(filePath, "rb").read())
    }
    encode_data = encode_multipart_formdata(file_data)
    uploadHeaders = {
        "Content-Type": encode_data[1],
        "Authorization": BotInfo.combine_Authorization(),
    }
    return uploadHeaders
