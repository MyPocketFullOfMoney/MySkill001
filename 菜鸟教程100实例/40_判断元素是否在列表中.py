'''
利用python的关键字in可以快速判断元素是否存在列表中
'''
# 时间：2021/2/22

if __name__ == '__main__':
    test_list = [1,3,5,2,6,8,'a',3]
    
    n = input('输入你想查看的值：')
    '''
    从键盘输入的n的值，类型为str
    当数字1，3，5从列表取出时，类型为int
    类型不同，导致in判断失败
    '''
    list_0 = test_list[0]
    print(type(n))
    print(type(list_0))
    # 这里对列表作类型转换
    if n in str(test_list) :
        print('存在')
    else :
        print('{0}不存在列表'.format(n))