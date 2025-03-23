class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"  # Base case

        result = "1"  # Starting term
        
        for _ in range(n - 1):  # Generate sequence up to n
            new_result = ""
            i = 0
            while i < len(result):
                count = 1  
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1 
                    i += 1
                new_result += str(count) + result[i]  
                i += 1  
            
            result = new_result  
        
        return result