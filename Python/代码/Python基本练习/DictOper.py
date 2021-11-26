import collections

"""
 练习字典的级别操作。
 1、创建字典
 2、增加元素，修改值
 3、获取所有key和值
 4、循环字典的技巧
"""
# 创建字典
info_dict = {"白酒指数": "10%", "新能源": "5%"}

# 增加一个元素，煤炭：6%
info_dict["煤炭"] = "6%"

print("字典info_dict:", info_dict)

# 获取所有的key
keys = info_dict.keys()
print("字典info_dict的keys:", keys)

# 循环字典的技巧
# info_dict.items以列表的形式返回一个视图对象
for k, v in info_dict.items():
    print("key:", k, "value:", v)




coll_list = ["a","a","a","b","c"]

count = collections.Counter(coll_list)

print("count的类型：",type(count))



print("count所有的key:",count.keys())


# 无法理解这行代码！
"""
 max(可迭代对象,[key=])
 当第一个参数为可迭代对象时，可以通过后面的key参数传入比较最大值的方法，通过该方法获取到最大值，返回可迭代对象中对应的值。
 例如max(dict.keys(),key=dict.get)
 dict.keys()：将字典中的键视图的方式返回，其中视图可迭代
 key=dict.get:将字典的get方法赋值给key。
 这样获取dict字典中键的最大值，比较方法为比较字典中值的最大值，比较完成后返回对应的键名。

"""
print(max(count.keys(),key=count.get))
