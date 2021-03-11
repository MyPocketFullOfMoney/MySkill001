"""
查找列表中最小的元素
时间：2021/3/11
"""
# 利用python自带的min函数
# 定义列表
num_List = [1,10,5,88,99]
print('列表的最小元素为：',min(num_List))

# 通过列表的sort函数排序，然后序列解包
num_List.sort()
print('列表的最小元素为：',*num_List[:1])