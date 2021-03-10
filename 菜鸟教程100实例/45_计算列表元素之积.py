"""
计算列表元素之积
时间：2021/3/10
"""
from typing import List

def multiplyList(myList:List[int]) -> int:
    result = 1
    for i_num in myList:
        result *= i_num
    return result

if __name__ == '__main__':
    t_list = [1,2,3,4]
    print(multiplyList(t_list))
