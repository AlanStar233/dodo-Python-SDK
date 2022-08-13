### 十二、公共请求头 Public_Headers

​	项目文件 -> [Public_Headers.py](../Public_Headers.py)

#### 12.1 Headers

##### 12.1.1 描述

​	公共请求头， 常规请求时用

##### 12.1.2 用法

​	**传参**： 不需要传参 (<s>甚至都不是方法</s>)

​	**调用**：

```python
import Public_Headers

my_headers = Public_Headers.Headers
```

​	**返回结果**：

| 返回参数 | 类型 | 描述 |
| -------- | ---- | ---- |
| -        | -    | -    |

#### 12.2 getUploadHeaders

##### 12.2.1 描述

​	公共请求头， 上传图片资源时用， 详见文件 -> [DoResourceUpload.py](../DoResourceUpload.py)

##### 12.2.2 用法

​	**传参**： fileName(可重赋的文件名，写什么都可以)、filePath(文件路径，请将路径转义)

​	**调用**：

```python
import Public_Headers

# 预定义, 或通过参数传递获得
fileName = "test.jpg"
filePath = "C:\\Users\\AAA\\Desktop\111.jpg"
Public_Headers.getUploadHeaders(fileName=fileName, filePath=filePath)
```

​	**返回结果**：

| 返回参数      | 类型 | 描述               |
| ------------- | ---- | ------------------ |
| uploadHeaders | dict | 经过组装后的请求头 |