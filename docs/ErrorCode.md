### 四、错误码 ErrorCode

​	项目文件 -> [ErrorCode.py](../ErrorCode.py)

#### 4.1 dodo_code()

##### 4.1.1 描述

​	解析传来的 status_code 并解析成对应的错误信息。

##### 4.1.2 用法

​	**传参**：status_code(dodo返回的状态码)

​	**调用**：

```python
import ErrorCode

# 一般 status_code 等同于解析传回信息 json 对象中的 status 属性
status_code = "-9999"
ErrorCode.dodo_code(status_code=status_code)
```

​	**返回结果**：

| 返回参数 | 类型 | 描述                                            |
| -------- | ---- | ----------------------------------------------- |
| message  | str  | 解释可以参照项目的 res 目录下的 error_code.json |

