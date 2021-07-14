class Solution:
    def isUnique_1(self,astr:str) -> bool:
        # 整型，26位
        mark = 0
        for char in astr:
            char_location = ord(char) - ord('a')
            if mark & (1<<char_location) != 0:
                return False
            else:
                mark |= (1<<char_location)
        return True

    def isUnique_2(self,astr:str) -> bool:
        return len(astr) == len(set(astr))

    def isUnique_3(self,astr:str) -> bool:
        i = 0
        for i in range(len(astr)):
            
            
            for j in range(i+1,len(astr)):
                if astr[i] == astr[j]:
                    return False
        return True