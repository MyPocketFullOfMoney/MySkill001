#Date:2020/6/29
#实现斐波那契数列

#定义一个函数
def fibonacci_fun(items:int):
    #第一项
    n1=0
    #第二项
    n2=1
    #循环从第三项开始
    count=2
    if items==1:
        print('斐波那契数列：',n1)
    elif items==0:
        print('请输入正整数！')
    else:
        print('斐波那契数列：')
        print(n1,',',n2,end=' , ')
        while count<items:
            nth=n1+n2
            print(nth,',',end=' ')
            n1=n2
            n2=nth
            count+=1

if __name__=='__main__':
    while True:
        try:
            x=int(input('你需要几项!\n'))
            fibonacci_fun(x)
            break
        except ValueError:
            print('请输入一个正整数！')

