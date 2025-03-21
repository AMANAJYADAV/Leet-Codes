class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.lstrip()
        if not s:
            return 0
       
        sign = 1
        i = 0
        if s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        return max(INT_MIN, min(num, INT_MAX))