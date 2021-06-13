
import ctypes

'利用模块ctypes获取内存地址中的值'
# 定义一个数字变量a
a = 10  
# 获取变量a的地址，赋给address
address = id(a)  
print('10的内存地址：',id(10))
# 把20赋值给变量a
a = 20
# 读取地址中的值
get_value = ctypes.cast(address, ctypes.py_object).value  
print('10的内存地址：',address,'从内存地址中取出的值：',get_value)
print('a的值：',a)

print('='*80)

a_list = [10] # 定义一个列表变量a_list，存在元素10

address_list = id(a_list)

print('a_list的内存地址：',address_list)

# 列表增加元素20
a_list[0] = 20

# 读取地址中的值
get_list_value = ctypes.cast(address_list, ctypes.py_object).value

print('列表的内存地址：',address_list,'从内存地址中取出的值：',get_list_value)
