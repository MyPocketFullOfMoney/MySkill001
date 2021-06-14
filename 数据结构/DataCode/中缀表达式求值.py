import re
from typing import List

def Solution(expre:str):
    '''利用两个栈，对中缀表达式求值'''

    # 运算对象栈
    opnd_stack = []

    # 运算符栈
    optr_stack =[]

    # 运算符优先级
    optr_dict = {'+':1,'-':1,'*':2,'/':2}
    # 遍历字符串，只能计算个位数的结果
    for i_expre in expre:

        # 利用正则模块匹配数字
        if re.match(r'\d+',i_expre):
            opnd_stack.append(i_expre)
        #左括号直接入optr栈，或栈不为空且栈顶元素未左括号，当前运算符直接入栈
        elif i_expre == '(' or (optr_stack and optr_stack[-1] == '('):
            optr_stack.append(i_expre)
        # optr栈为空，或栈顶运算符优先级小于当前运算符，当前运算符入栈
        elif not optr_stack or (i_expre != ')' and optr_dict[optr_stack[-1]] < optr_dict[i_expre]):
            optr_stack.append(i_expre)
        # optr栈不为空，且栈顶运算符优先级大于等于当前运算符。optr栈顶元素出栈，
        # opnd出栈两个运算对象
        elif optr_stack and i_expre != ')' and optr_dict[optr_stack[-1]] >= optr_dict[i_expre]:
            # 计算结果
            result = calculation(optr_stack,opnd_stack)
            #当前运算符入栈
            optr_stack.append(i_expre)
            opnd_stack.append(result)
        # 遇到右括号，要一直出栈，直到匹配左括号
        elif i_expre == ')':
            while optr_stack[-1] != '(':
                result = calculation(optr_stack,opnd_stack)
                opnd_stack.append(result)
            # 出栈左括号
            optr_stack.pop()
    # 最后运算符栈必然为空，如果不为空则计算未完成
    if optr_stack:
        result = calculation(optr_stack,opnd_stack)
        opnd_stack.append(result)
    print(optr_stack)
    return opnd_stack



def calculation(optr_stack:List,opnd_stack:List):
    # 出栈运算符
    optr = optr_stack.pop()
    # 运算符右侧对象
    right_obj = opnd_stack.pop()
    # 运算符左侧对象
    left_obj = opnd_stack.pop()
    
    if optr == '+':
        return int(left_obj) + int(right_obj)
    elif optr == '-':
        return int(left_obj) - int(right_obj)
    elif optr == '*':
        return int(left_obj) * int(right_obj)
    else:
        return int(left_obj) / int(right_obj)

        
if __name__ == '__main__':
    exper = '5-3+9*6*(6-1-2)'

    print(Solution(exper))
