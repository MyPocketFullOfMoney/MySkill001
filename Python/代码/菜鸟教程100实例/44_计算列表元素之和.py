'''
利用for、while循环以及递归的方法计算列表元素的和
时间：2021/3/4
'''
from typing import List 

c_list = [1,3,2,8,10]

# 通过for循环计算
total_for = 0
for i_num in c_list:
    total_for += i_num

print('for循环实现元素之和total_for=',total_for)

# 通过while循环计算
total_while = 0
l_iter = 0
while l_iter < len(c_list):
    total_while = total_while + c_list[l_iter]
    l_iter += 1
print('while循环实现元素之和total_while=',total_while)

# 通过递归实现
def sumofList(list:List[int],size:int) -> int:
    # 递归函数最重要的就是结束条件的判断
    if (size == 0):
        return 0
    else:
        return list[size-1] + sumofList(list,size-1)
total_r = sumofList(c_list,len(c_list))
print('递归实现元素之和total_r=',total_r)