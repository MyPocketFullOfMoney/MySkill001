class Solution:
    """
    虾皮面试题：Excel列号转换为对应的数字，A,B,C.....AA,AB,AB对饮1，2，3......,27,28,29
    """
    def Exceltonum(self,s:str):
        if not s:return None
        # 将字符同一转换为大写
        s = s.upper()
        s = list(s)
        # 创建26个字母
        chars = [chr(x) for x in range(65,91)]
        # 每个字母对应的值
        nums = [ n+1 for n in range(26)]
        # 组成字典
        dicts = dict(zip(chars,nums))
        print(s,'\n',dicts)
        str_n = 0
        res = 0
        
        while s:
            '输入的字符串转换为列表，从低为开始算，每算一个，移除一个，直到列表为空，结束循环。'
            tmp = dicts[s[-1]]
            res += tmp*pow(26,str_n)
            s.pop()
            str_n += 1
        print(res)


if __name__ == '__main__':
    test = Solution()
    test.Exceltonum("ad")