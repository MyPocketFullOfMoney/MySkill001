import re
from typing import List

def change_exper(exper):
    '''中缀表达式转后缀表达式'''
    
    # 运算符栈
    optr_stack = []
    
    # 存放结果
    result_stack = []
    
    # 运算符优先级
    optr_prio_dict = {'+':1,'-':1,'*':2,'/':2}

    # 判断正负
    Isoptr = True

    tmp = ''
    mid = ''
    
    # 遍历字符串
    for i_exper in exper:
        # 如果为‘-’，需要判断是减号还是负号。
        # 第一个数为负数，运算符栈为空；左括号后跟'-'，代表负数。
        if (exper.index(i_exper) == 0 and i_exper == '-') or (i_exper == '-' and optr_stack and tmp == '(') :
            Isoptr = False
            continue
        # 如果为数字，直接入结果栈
        if re.match(r'\d+', i_exper):
            if not Isoptr:
                Isoptr = True
                result_stack.append('-'+i_exper)
            else:
                result_stack.append(i_exper)
        # 如果等于左括号，直接入运算法栈
        elif i_exper == '(' or (optr_stack and optr_stack[-1] == '('):
            optr_stack.append(i_exper)
        # 运算符栈为空，运算符直接入栈或者当前运算符优先级大于栈顶运算符
        elif not optr_stack or ( i_exper != ')' and optr_prio_dict[i_exper] > optr_prio_dict[optr_stack[-1]]):
            optr_stack.append(i_exper)
        # 运算符为右括号，运算符栈一直出栈，直到匹配左括号
        elif i_exper == ')':
            while optr_stack[-1] != '(':
                result_stack.append(optr_stack.pop())
            # 左括号出栈
            optr_stack.pop()
        # 运算符栈不为空且当前运算符优先级小于等于栈顶元素优先级，栈顶元素出栈
        elif optr_stack:
            while True:
                result_stack.append(optr_stack.pop())
                if not optr_stack or optr_stack[-1] == '(' or optr_prio_dict[i_exper] > optr_prio_dict[optr_stack[-1]]:
                    break
            # 当前运算符入运算符栈
            optr_stack.append(i_exper)
        tmp = i_exper
    # 遍历玩表达式，运算符栈要为空
    if optr_stack:
        while optr_stack:
            result_stack.append(optr_stack.pop())
    #print(result_stack)
    return result_stack

def exper_calcu(exper_list:List):
    '''后缀表达式求值'''
    
    calcu_result = []
    
    for n in exper_list:
        
        if  re.match(r'\d+|-\d+', n):
            calcu_result.append(n)
        elif n == '+':
            right_num = int(calcu_result.pop())
            left_num = int(calcu_result.pop())
            calcu_result.append(left_num + right_num)
        elif n == '-':
            right_num = int(calcu_result.pop())
            left_num = int(calcu_result.pop())
            calcu_result.append(left_num - right_num)
        elif n == '*':
            right_num = int(calcu_result.pop())
            left_num = int(calcu_result.pop())
            calcu_result.append(left_num * right_num)
        else:
            right_num = int(calcu_result.pop())
            left_num = int(calcu_result.pop())
            calcu_result.append(left_num / right_num)
        #print(calcu_result)
    return calcu_result[-1]

def main():
    #t_str = input()
    #t_str = '3*5+8-0*3-6+0+0'
    #t_str = '3+2*{1+2*[-4/(8-6)+7]}'
    t_str = '5-3+9*6*(6-10-2)'

    if re.findall(r'[^0-9\+\-\*\/\(\)\[\]\{\}]', t_str):
        exit()
    else:
        # {}、[]括号替换为()
        t_str = re.sub(r'[\{\[]','(',t_str)
        t_str = re.sub(r'[\}\]]',')',t_str)

        t_str = t_str.replace('+',' + ')
        t_str = t_str.replace('-',' - ')
        t_str = t_str.replace('*',' * ')
        t_str = t_str.replace('/',' / ')
        t_str = t_str.replace('(',' ( ')
        t_str = t_str.replace(')',' ) ')

        a = t_str.split()

        m = change_exper(a)
        print(exper_calcu(m))

if __name__ == '__main__':

    main()