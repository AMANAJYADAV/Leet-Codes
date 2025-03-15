class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s  # Edge case: empty string or single character

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindrome substring

        longest_palindrome = ""
        
        for i in range(len(s)):
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome

            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome