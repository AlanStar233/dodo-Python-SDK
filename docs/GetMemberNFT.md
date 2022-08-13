### 八、获取群成员NFT

​	项目文件 -> [GetMemberNFT.py](../GetMemberNFT.py)

#### 8.1 getMemberNFTStatus()

##### 8.1.1 描述

​	获取用户 NFT 状态

##### 8.1.2 用法

​	**传参**：islandId(群号), dodoId(dodo号), platform(平台), issuer(发行方), series(类别)

> **platform 参数** :	高能链 -> upower	优版权 -> ubanquan	MetaMask -> metamask

​	**调用**：

```python
import GetMemberNFT

# 预定义, 或通过参数传递获得
islandId = 23333
dodoId = 11111
platform = "upower"
issuer = "哔哩哔哩"
series = "鸽德"
GetMemberNFT.getMemberNFTStatus(islandId=islandId, dodoId=dodoId, platform=platform, issuer=issuer, series=series)
```

​	**返回结果**：

| 返回参数    | 类型 | 描述        |
| ----------- | ---- | ----------- |
| NFT_message | dict | NFT数据信息 |