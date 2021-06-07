
def print_tuple(*name):
    '以元组的方式传入参数'
    name_len = len(name)
    print('参数个数：', name_len)
    print('*name的类型', type(name))
    print('*name的值：', name)
    n = 0
    # 遍历参数，输出每个参数的值
    for i_name in name:

        print('第{n}个名字：{value}'.format(n=n, value=i_name))
        n += 1


def print_dict(**kwargs):
    '以字典的方式传入参数'
    k_len = len(kwargs)
    print('参数个数：', k_len)
    print('**kwargs的类型：', type(kwargs))
    print('**kwargs的值：', kwargs)
    n = 0
    # 遍历参数字典
    for k_name, v_name in kwargs.items():
        print('{}:{}'.format(k_name, v_name))


def print_fenge():
    print('='*60)


if __name__ == '__main__':
    name_1 = 'test'
    name_2 = 'Python'
    name_3 = 'MySQL'
    name_4 = '计算机网络'

    # 传入4个参数，但在函数中4个参数的值以元组的形式存放
    print('元组作为参数，传入四个变量：')
    print_tuple(name_1, name_2, name_3, name_4)

    print_fenge()

    # 传入4个参数，注意赋值方式
    print('字典作为参数，传入四个变量：')
    print_dict(name_1='TEST', name_2='PYTHON', name_3='MYSQL', name_4='计算机网络2')

    # 定义一个元组，元组里有4个元素
    name_tuple = ('test', 'Python', 'MySQL', '计算机网络')

    print_fenge()

    # name_tuple元组带*为参数
    print('元组作为参数，传入一个元组变量，带*号：')
    print_tuple(*name_tuple)

    print_fenge()

    # name_tuple元组不带*为参数
    print('元组作为参数，传入一个元组变量，带*号：')
    print_tuple(name_tuple)

    # 定义一个字典，有4个键值对
    name_dict = {'name_1': 'TEST', 'name_2': 'PYTHON',
                 'name_3': 'MYSQL', 'name_4': '计算机网络2'}

    print_fenge()

    # name_dict字典带**号作为参数
    print('字典作为参数，带**号传入')
    print_dict(**name_dict)

    print_fenge()

    # name_dict字典不带**号作为参数，会报错！
    try:
        print('字典作为参数，不带**号传入')
        print_dict(name_dict)
    except Exception as error_info:
        print('错误信息：', error_info)
