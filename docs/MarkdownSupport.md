### 十一、dodo Markdown 支持 MarkdownSupport

​	项目文件 -> [MarkdownSupport.py](../MarkdownSupport.py)

> **注：由于返回信息均为 str 型 的message，故不重复解释。**

#### 11.1 bold()

##### 11.1.1 描述

​	粗体

##### 11.1.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.bold(message)
```

#### 11.2 italic()

##### 11.2.1 描述

​	斜体

##### 11.2.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.italic(message)
```

#### 11.3 baseline()

##### 11.3.1 描述

​	底线

##### 11.3.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.baseline(message)
```

#### 11.4 link()

##### 11.4.1 描述

​	链接

##### 11.4.2 用法

​	**传参**：desc(URL描述)、url(URL)

​	**调用**：

```python
import MarkdownSupport

desc = "这是一个链接"
url = "https://www.bilibili.com"
MarkdownSupport.link(desc, url)
```

#### 11.5 delLine()

##### 11.5.1 描述

​	删除线

##### 11.5.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.delLine(message)
```

#### 11.6 anti_spoilers()

##### 11.6.1 描述

​	防剧透

##### 11.6.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.anti_spoilers(message)
```

#### 11.7 quote()

##### 11.7.1 描述

​	引用

##### 11.7.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.quote(message)
```

#### 11.8 code_block()

##### 11.8.1 描述

​	代码块

##### 11.8.2 用法

​	**传参**：message(欲加工的字符串)

​	**调用**：

```python
import MarkdownSupport

message = "hello DoDo !"
MarkdownSupport.code_block(message)
```

#### 11.9 at_user()

##### 11.9.1 描述

​	艾特用户

##### 11.9.2 用法

​	**传参**：dodoId(dodo号)

​	**调用**：

```python
import MarkdownSupport

dodoId = 11111
MarkdownSupport.at_user(dodoId)
```

#### 11.10 jump_channel()

##### 11.10.1 描述

​	跳转频道

##### 11.10.2 用法

​	**传参**：channelId(频道ID)

​	**调用**：

```python
import MarkdownSupport

channelId = 22222
MarkdownSupport.jump_channel(channelId)
```

