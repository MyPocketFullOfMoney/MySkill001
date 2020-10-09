# filename:最小公倍数算法
# 时间：2020年10月9日

# 定义函数
def lcm(x,y):
    # 获取较大的数
    if x > y :
        greater = x
    else:
        greater = y
    
    # 从较大的数开始循环，每次+1，符合条件推出循环
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

if __name__ == '__main__':
    num_1 = int(input('输入第一个整数：'))
    num_2 = int(input('输入第二个整数：'))
    print('最小公倍数为：',lcm(num_1,num_2))