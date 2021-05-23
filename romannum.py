class Solution:
    def romanToInt(self , s ):
        # write code here
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,\
                     'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sum = 0
        for i_roman in range(len(s)):
            if s[i_roman] in roman_dict.keys():
                r_value = roman_dict[s[i_roman]]
                                
                if i_roman >0 and s[i_roman-1] + s[i_roman] in roman_dict.keys():
                    sum = sum - roman_dict[s[i_roman-1]]
                    r_value = roman_dict[s[i_roman-1] + s[i_roman]]

            sum += r_value
        return sum

if __name__ == '__main__':
    
    test = Solution()
    print(test.romanToInt("MCMXCIV"))
