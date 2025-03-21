class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() 
        queue = deque([(0, 0, [])])  
        res = []

        while queue:
            total, start, path = queue.popleft()

            if total == target:
                res.append(path)
                continue  
            
            for i in range(start, len(candidates)):
                new_total = total + candidates[i]

                if new_total > target:
                    break  

                queue.append((new_total, i, path + [candidates[i]]))  

        return res