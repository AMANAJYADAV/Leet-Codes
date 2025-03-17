class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = list(range(1, n + 1))
        
        # Step 2: Compute factorials to determine the size of each group
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        
        k -= 1
        
        result = []
        for i in range(n - 1, -1, -1):
            index = k // fact[i]  
            result.append(str(numbers[index]))  
            numbers.pop(index) 
            k %= fact[i]  

        return "".join(result)  