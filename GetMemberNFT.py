import json

import requests

import Public_Headers

# 获取用户 NFT 状态
def getMemberNFTStatus(islandId, dodoId, platform, issuer, series):
    URL = "https://botopen.imdodo.com/api/v1/member/nft/status"
    public_headers = Public_Headers.Headers

    # platform
    # 高能链: upower   优版权: ubanquan   MetaMask: metamask
    NFT_data = {
        "islandId": islandId,
        "dodoId": str(dodoId),
        "platform": str(platform),
        "issuer": str(issuer),
        "series": str(series)
    }

    # 发送请求
    NFT_message = requests.post(URL, headers=public_headers, data=json.dumps(NFT_data))
    NFT_message = NFT_message.text
    NFT_message = json.loads(NFT_message)

    # 数据解析
    status = NFT_message["status"]
    message = NFT_message["message"]

    # 是否已绑定该数字藏品平台  0: 否    1: 是
    isBandPlatform = NFT_message["data"]["isBandPlatform"]
    # 是否拥有该发行方的NFT  0: 否    1: 是
    isHaveIssuer = NFT_message["data"]["isHaveIssuer"]
    # 是否拥有该系列的NFT  0: 否    1: 是
    isHaveSeries = NFT_message["data"]["isHaveSeries"]

    # 返回 json
    return NFT_message


if __name__ == "__main__":
    islandId = 29118
    dodoId = 254913173
    platform = "upower"
    # 查询用户是否拥有 高能链 下的 鸽德 NFT
    print(getMemberNFTStatus(islandId=islandId, dodoId=dodoId, platform=platform, issuer="哔哩哔哩", series="鸽德"))