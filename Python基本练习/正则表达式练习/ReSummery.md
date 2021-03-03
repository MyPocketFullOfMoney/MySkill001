# RE模块  
>内存数据库中存在许多表，但测试环境的业务程序可能只使用了一部分。因此希望利用re模块，从业务程序的sql配置文件中匹配出表名，再依据表名获取到对应的建表语句。
当测试环境新建内存库时，就能减少表的创建，从而减少内存空间的浪费。


首先导入re模块
```python
import re
```
本次主要利用了re的两个方法，`re.findall()、re.sub()`，下面是这两个方法的简单介绍。
## findall方法介绍
### 描述
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表；如果没有匹配成功，则返回空列表。  
### 语法格式
>re.findall(pattern,string,flags=0)
### 参数：
- `pattern`匹配模式。
- `string`待匹配字符串。
- `flags`正则表达式修饰符-可选标志
     - `re.I`使匹配对大小写不敏感
     - `re.S`使.匹配包括换行在内的所有字符
### 代码实例
```python
    r"""
    匹配四中场景：
      from abc on:只要查询语句走索引，无论有无where条件，都能匹配 
      from abc where：查询有where条件，但不走索引
      from abc\s\n：查询语索引，也没有where条后面跟空白字符后换行
      from abc\n：查询语句引，也没有where条件直接换行
    """
    name_list = re.findall(r+from.*\s+on|\s+from.+where\b|\s+from\s+\w+$+from\s+\w+\s+content_line,re.I)
```
## sub方法介绍  
### 描述  
re.sub用于替换字符串中的匹配项
### 语法：
>re.sub(pattern, repl, string, count=0, flags=0)
### 参数：
- pattern：正则中的模式字符串。
- repl：替换的字符串，也可为一个函数。
- string：要被查找替换的原始字符串。
- count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。
- flags：编译时用的匹配模式，数字形式。

前三个为必选参数，后两个为可选参数。
### 代码实例
```python
# 除去from、where、on关键字，空格,where开头，on结尾的字符串
    name_tab = re.sub(r'\s+where.*\bon|\s+from\s+|\s+on|\s+where','',name_str,flags=re.I)
 
```
**注意**
>当使用标志位却没有匹配次数的参数时，标志位参数必须为`flags=re.I`才能生效  

**错误代码**
```python
    # 这是错误的！！！！
    # 无法忽略大小写
    str = re.sub(pattern,repl,string,re.I)
```
**正确代码**
```python
    # 匹配时会忽略字符的大小写
    str = re.sub(pattern,repl,string,flags=re.I)
```

更多内容可以参考 **[菜鸟教程](https://www.runoob.com/python3/python3-reg-expressions.html)** 正则表达式部分.