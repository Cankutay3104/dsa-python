# LeetCode '13. Roman to Integer' Solution

class Solution(object):
    def romanToInt(self, s):
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        
        number = 0
        for i in range(len(s)):
            curChar = s[i]
            curVal = romans[curChar]
            if i < len(s)-1 and romans[s[i+1]] > curVal:
                number -= curVal
            else:
                number += curVal

        return number