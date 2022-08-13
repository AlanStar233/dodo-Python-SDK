### 三、资源上传 DoResourceUpload

​	项目文件 -> [DoResourceUpload.py](../DoResourceUpload.py)

#### 3.1 图片上传

##### 3.1.1 描述

​	上传目标文件。

##### 3.1.2 用法

​	**传参**：filePath(文件路径, 请使用**转义路径**)、fileName(文件名，可以另起名字)

​	**调用**：

```python
import DoResourceUpload

# 预先声明参数或自行获取
# 路径可用相对或绝对路径，绝对路径请使用 \\ 来代替 \
filePath = "C:\\Users\\AAA\\Desktop\\pic.jpg"
fileName = "my_pic.jpg"
DoResourceUpload.pic_upload(filePath=filePath, fileName=fileName)
```

​	**返回结果**：

| 返回参数     | 类型 | 描述               |
| ------------ | ---- | ------------------ |
| file_message | dict | 上传成功与否的消息 |