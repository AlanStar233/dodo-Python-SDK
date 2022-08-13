### 十三、身份行为 RoleAction

​	项目文件 -> [RoleAction.py](../RoleAction.py)

#### 13.1 getRoleList

##### 13.1.1 描述

​	获取身份组列表

##### 13.1.2 用法

​	**传参**：islandId(群号)

​	**调用**：

```python
import RoleAction

# 预定义, 或通过参数传递获得
islandId = 22222
RoleAction.getRoleList(islandId=islandId)
```

​	**返回结果**：

| 返回参数  | 类型 | 描述       |
| --------- | ---- | ---------- |
| role_info | dict | 身份组列表 |

#### 13.2 setRole

##### 13.2.1 描述

​	赋予成员身份组

##### 13.2.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)、roleId(身份组ID)

​	**调用**：

```python
import RoleAction

# 预定义, 或通过参数传递获得
islandId = 22222
dodoId = 11111
roleId = 2333
RoleAction.setRole(islandId=islandId, dodoId=dodoId, roleId=roleId)
```

​	**返回结果**：

| 返回参数  | 类型 | 描述     |
| --------- | ---- | -------- |
| role_info | dict | 操作信息 |

#### 13.3 removeRole

##### 13.3.1 描述

​	移除成员身份组

##### 13.3.2 用法

​	**传参**：islandId(群号)、dodoId(dodo号)、roleId(身份组ID)

​	**调用**：

```python
import RoleAction

# 预定义, 或通过参数传递获得
islandId = 22222
dodoId = 11111
roleId = 2333
RoleAction.removeRole(islandId=islandId, dodoId=dodoId, roleId=roleId)
```

​	**返回结果**：

| 返回参数  | 类型 | 描述     |
| --------- | ---- | -------- |
| role_info | dict | 操作信息 |