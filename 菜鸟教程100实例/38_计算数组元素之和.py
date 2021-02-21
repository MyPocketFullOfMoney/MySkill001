"""
定义一个整型数组，并计算元素之和
例子：
输入 : arr[] = {1, 2, 3}
输出 : 6
计算: 1 + 2 + 3 = 6 
"""
# 时间：2021/2/21
# 用list表示数组，调用内置函数sum求和
from typing import List
# 定义函数_sum，有两个参数，arr为数组，n为长度
def _sum(arr:List[int],n):
    return sum(arr)

if __name__ == "__main__":
    test = [12,3,4,5]
    # 获取长度
    n = len(test)
    # 调用函数_sum
    result = _sum(test,n)

    # 输出结果
    print('数组：',test)
    print('数组元素之和为：',result)