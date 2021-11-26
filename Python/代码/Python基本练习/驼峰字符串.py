import re
class Solution:
    def camelCase(self , newString ):
        # write code here
        res = 'shopee'
        if not newString: return res
        temp = []
        index = []
        j = 0
        for i in list(newString):
            if  re.findall(r'[a-zA-Z0-9]',i) :
                j += 1
                temp.append(i.loewr())
            else:
                index.append(j)
        
        for k in index:
            if k < len(temp) and k != 1:
                temp[k] = temp[k].upper()
                 
        return ''.join(temp)


if __name__ == '__main__':
    test = Solution()
    print(test.camelCase("_hello_word_word"))