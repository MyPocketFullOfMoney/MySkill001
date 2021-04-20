# 利用函数的方式实现，获取两数间的最大公约数

# 定义函数
def hcf(x,y):
    # 先比较两个数大小，最大公约数只能是较小的一个数
    if x < y:
        smaller = x
    else:
        smaller = y
    
    # 通过循环的方式获取最大公约数
    for i in range(1,smaller+1):
        # hcf可能会被多次赋值，但是i是递增的，循环结束，记录最后一次赋值即可
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# main函数
if __name__ == '__main__':
    # 用户输入两个数字
    num_1 = int(input('输入第一个数字：'))
    num_2 = int(input('输入第二个数字：'))
    print('最大公约数为：',hcf(num_1,num_2))