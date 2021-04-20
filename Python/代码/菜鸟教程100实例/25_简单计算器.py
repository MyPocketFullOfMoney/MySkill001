# 简单计算器的实现
# 2020/10/13

# 定义类
class Calculator:
    
    # 支持符合合集
    symbo = ['+','-','*','/']

    # 获取用户输入
    def get_user_num(self):
        num_1 = int(input('输入第一个整数：'))
        num_2 = int(input('输入第二个整数：')) 
        note = str(input('请输入操作符(只限于这四种+、-、*、/): '))  
        # 获取用户计算方式，目前支持：+、-、*、/,4种运算
        if note not in self.symbo:
            print('输入错误！退出！')
            exit
        else:

            # 计算结果
            result = self.get_calculation(note,num_1,num_2)

            # 输出计算表达式
            print('计算结果为：',num_1,note,num_2,'=',result)
            
    
    # 计算结果
    def get_calculation(self,note_str:str,x,y):
        if note_str == '+':
            return x + y
        if note_str == '-':
            return x - y
        if note_str == '*':
            return x * y
        if note_str == '/':
            return x / y

    







# main函数
if __name__ == '__main__':
    # 类的实例化
    demo = Calculator()
    demo.get_user_num()