class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # 创建字典，通过右括号，找出对应的左括号
        bracket_dict = {'}':'{',')':'(',']':'['}

        for bracket_i in s:

            if len(s) % 2 == 1 :
                return False
            # 栈不为空的情况下，当遇到右括号，栈顶元素需要出栈
            if  bracket_i in bracket_dict and stack:
                if bracket_dict[bracket_i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                # 左括号直接入栈
                stack.append(bracket_i)

        # 栈为空，完全匹配
        return not stack