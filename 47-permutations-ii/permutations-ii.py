class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue  
                seen.add(nums[i])

                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res
