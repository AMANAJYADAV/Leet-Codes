class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False

        def isInteger(s):
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            if '.' not in s:
                return False
            integer, _, fraction = s.partition('.')
            if not integer and not fraction:
                return False
            if integer and not integer.isdigit():
                return False
            if fraction and not fraction.isdigit():
                return False
            return True

        if 'e' in s or 'E' in s:
            base, _, exp = s.partition('e') if 'e' in s else s.partition('E')
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        return isInteger(s) or isDecimal(s)