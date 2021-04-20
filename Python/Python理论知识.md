# 目录  

<!-- TOC -->

- [目录](#目录)
  - [模块](#模块)
    - [1、模块的定义](#1模块的定义)
    - [2、import语句导入模块](#2import语句导入模块)
    - [3、from ... import 语句](#3from--import-语句)
    - [4、__name__属性](#4__name__属性)
    - [5、包](#5包)

<!-- /TOC -->

## 模块  

### 1、模块的定义  

模块是一个包含所有你定义的函数和变量的文件，其后缀名是\. py。模块可以被别的程序引入，以使用该模块中的函数等功能。

### 2、import语句导入模块  

`import module1[,module2[,...moduleN]`  
当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。  

Python导入的模块是根据搜索路径来搜索文件的。Python的搜索路径存储在sys模块中的path变量中。  

输出path变量：

```python
    import sys
    print(sys.path)
```

`sys.path`输出是一个列表。在脚本中可以通过`sys.path.append([路径])`来修改搜索路径，从而引入一些不存在搜索路径中的模块。

**例子**  
目录结构

```shell
test  
  - support.py  
  - test.py
```

**support\. py**  
文件代码

```python
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return
```

**test\. py**
文件代码  

```python
# Filename: test.py
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
```

当运行`test.py`文件时，  
输出结果`Hello：Runoob`  

因为test.py文件和support.py文件在同一个目录，当运行test.py文件时，解释器会检索脚本运行的当前目录，所以support模块被导入到test.py文件中。因为`import support`语句并没有指明导入什么函数，所以访问`print_func`函数时，需要通过模块名访问。  

### 3、from ... import 语句  

from语句让你从模块中导入一个指定的部分到当前命名空间。  
语法：  
`from modname import name1[,name2[,...nameN]]`  
**例子**  
`from support import print_fun`  
从`support.py`文件中导入`print_fun`函数  

### 4、__name__属性  

每个模块都有一个__name__属性，当其值是\` \_\_main\_\_ \`时，表明该模块自身在运行，否则是被引入。  

### 5、包  

目录只有包含一个叫做`__init__.py`的文件才会被认作是一个包。  
