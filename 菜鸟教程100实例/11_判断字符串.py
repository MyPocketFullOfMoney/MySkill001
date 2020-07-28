#coding=utf-8 Python 3.7.4
''' 
 * Description  : 判断字符串是否由数字组成
 * Author       : Lichongyou
 * Date         : 2020-07-28 15:23:24
 * LastEditTime : 2020-07-28 17:19:34
 * LastEditors  : Lichongyou
''' 

# 通过函数的方式实现
def is_number(s:str):
    # 利用Pytho内置的异常类型
    try:
        print('字符串：',s)
        float(s)
        return True
    except ValueError:
        pass
    # Uncidoe字符集
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError,ValueError):
        pass

    return False



if __name__ == "__main__":
    # 测试数字和字符串
    print('结果  ：',is_number('foo'))
    print('结果  ：',is_number('123'))

    # 测试 Unicode
    # 阿拉伯语 5
    print('结果  ：',is_number('٥'))  # True
    # 泰语 2
    print('结果  ：',is_number('๒'))  # True
    # 中文数字
    print('结果  ：',is_number('四')) # True
    # 版权号
    print('结果  ：',is_number('©'))  # False