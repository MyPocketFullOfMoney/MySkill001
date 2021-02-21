'''
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。

例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。

以下演示了将数组的前面两个元素放到数组后面。

原始数组: ori = [1,2,3,4,5,6,7]

翻转后：result = [3,4,5,6,7,1,2]


'''

# 时间：2021/2/21
from typing import List

# 定义函数turn_list,参数arr表示数组,n为翻转的个数
'''
利用python列表切片的方法，把要翻转的List，分割为List_1[0,n],List_2[n:]
然后组合成新的列表result = List_2 + List_1
但是会有例外情况，当想全部翻转时，无法通过切片重组列表.
'''
def turn_list(arr:List[int],n) -> List[int]:
    # python的列表0-n，不包含n本身
    List_1 = arr[0:n]
    List_2 = arr[n:]

    return List_2 + List_1

if __name__ == "__main__":
    test_l = [1,2,3,4,5,6,7]
    print('测试数组：',test_l)
    n = int(input('输入需要翻转的个数：'))
    if n < len(test_l):
        # 调用函数turn_list
        result = turn_list(test_l,n)
        # 输出结果
        print('结果：',result)
    elif n == len(test_l):
        test_l.reverse()
        # 输出结果
        print('结果：',test_l)
    else:
        print('输入错误！！！')