# 目录  

<!-- TOC -->

- [目录](#目录)
  - [模块](#模块)
    - [1、模块的定义](#1模块的定义)
    - [2、import语句导入模块](#2import语句导入模块)
    - [3、from ... import 语句](#3from--import-语句)
    - [4、__name__属性](#4__name__属性)
    - [5、包](#5包)
  - [Python常用的数据结构](#python常用的数据结构)
    - [字符串](#字符串)
      - [字符串格式化](#字符串格式化)
        - [python字符串格式化符号](#python字符串格式化符号)
        - [实例](#实例)
        - [str.format()函数](#strformat函数)
        - [应用场景](#应用场景)
    - [列表](#列表)
    - [元组](#元组)
    - [元组的解包](#元组的解包)
    - [集合](#集合)
    - [字典](#字典)
  - [赋值、浅拷贝、深拷贝的区别](#赋值浅拷贝深拷贝的区别)
  - [函数](#函数)
    - [函数的定义](#函数的定义)
    - [函数的传参方式](#函数的传参方式)
  - [面向对象](#面向对象)
    - [类的定义](#类的定义)
    - [类的成员](#类的成员)
    - [类方法](#类方法)
  - [迭代器和生成器](#迭代器和生成器)
  - [装饰器](#装饰器)
  - [上下文管理器](#上下文管理器)
  - [多线程](#多线程)
  - [参考资料](#参考资料)

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

## Python常用的数据结构

在Python有六个标准数据类型：

- **不可变数据类型**：Number（数字）、String（字符串）、Tuple（元组）;
- **可变数据类型**：List（列表）、Dictionary（字典）、Set（集合）。

**个人理解**，所谓的不可变，指的是通过变量的赋值，无法改变同一内存地址的值。

例如：

a = 10，a指向的内存地址为12345;对变量a再进行赋值，a = 20，a指向的内存地址为6553。
从内存地址12345取出的值仍然是10，对变量a的赋值操作并没有改变内存地址12345的值。

而当数据为可变类型时，a_list = [10]，a_list指向内存地址2000；向a_list列表添加元素20，a_list.append(20)，a_list指向的内存地址仍然是2000，但通过内存地址取出的值已经变成了[10,20]

**元组不可变，指的是存放的内容不能被改变。**

从内存角度理解，当元组中的元素为列表时，为什么能修改列表？

`t_tuple = ([1,2,3],'a')`

当元组的元素为列表`[1,2,3]`时，元组保存的是指向列表`[1,2,3]`的内存地址，对列表进行增加和删除元素，并不会改变列表的内存地址。

相当于

```python
  a_list = [1,2,3]
  t_tuple = (a_list,'a')
```

### 字符串

#### 字符串格式化

##### python字符串格式化符号

| 符号 | 描述 |
| ---- | ---- |
| %s | 格式化字符串 |
| %d | 格式化整数 |

##### 实例

```python
    t_str = 'My name is %s'
    result = t_str%'test'
    print(result)
```

输出结果
>My name is test

##### str.format()函数

`format`函数可以接受不限个参数，位置可以不按顺序。
参数类型可以是列表、字典、对象

```python
    # 通过字典设置参数
i_dict = {'name':'python','age':'18'}
t_str = 'My name is {name},age {age}'

print(t_str.format(**i_dict))


# 通过列表索引设置参数
i_list = ['test','18']
t_str = 'My name is {0[0]},age {0[1]}'

print(t_str.format(i_list))
```

输出结果
>My name is python,age 18  
>My name is test,age 18

##### 应用场景

1. python操作mysql，批量生成测试数据。

  ```python
    # 打开数据库连接
    with pymysql.connect(host="127.0.0.1", user="root", passwd="123456",     database="data_li") as db:
        # 获取游标
        cursor = db.cursor()
    
        # sql语句
        sql = '''insert into employee (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
            values ('Huawei','Rongyao',{0[0]},'M',{0[1]})
            '''
    
        for i in range(1, 11):
            i_list = [i, i+400]
            # 执行
            cursor.execute(sql.format(i_list))
        # 提交
        db.commit()
  ```

### 列表

### 元组

### 元组的解包

### 集合

### 字典

## 赋值、浅拷贝、深拷贝的区别

## 函数

### 函数的定义

```python
def function_name(parameter_1,parameter_2):
    函数体
```

### 函数的传参方式

- 以元组为参数，在参数名前加\*号表示区别。
- 以字典为参数，在参数名前加\*\*号表示区别。

## 面向对象

### 类的定义

```python
  class ClassNaem:
    '''这是一个people类'''
    # 这是一个类变量，在整个实例化的对象中共用
    i_class = 1
    
    # 定义构造函数
    def __init__(self,i_num):
      # i_self是一个实例变量
      self.i_self = i_num
    .
    .
    <statement-n>
```

### 类的成员

一个类中成员可以有变量和方法。其中以双下划线开头的成员为私有变量或方法。

### 类方法

类方法中，必须有一个额外的**第一个参数名称**，按照惯例第一个参数命名为self，代表实例本身。

self并不是Python的关键字，我们用其它名字命名也行。

## 迭代器和生成器

### 迭代器

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素都被访问结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter()和next()

### 生成器

在Python中，使用了**yield**的函数被称为生成器（generator）。

生成器是一个返回迭代器的函数，只能用于迭代操作，更简单的理解生成器就是一个迭代器。

在调用生成器的过程中，每次遇到yeild时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。

## 装饰器

## 上下文管理器

### 上下文管理器的作用

1. 管理资源，如文件操作、数据库连接;
2. 更优雅的处理异常

### 实现的方式

通过类实现上下文管理，在类中实现`__enter__()`和`__exit__()`的方法，这个类的实例就是上下文管理器。

其中`__exit__(self,exc_type,exc_value,exc_tb)`方法中包含三个参数exc_type、exc_value、exc_tb，它们的含义分别为：

- exc_type：异常类型
- exc_value：异常值
- exc_tb：异常的错误栈信息

在`__exit__()`方法中，如果返回True，则表示发生的异常已经被处理，程序会继续执行with代码块之后的代码。

## 多线程

## 参考资料

[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)

[上下文管理器](https://www.cnblogs.com/wongbingming/p/10519553.html)
