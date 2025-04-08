class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        inserted = False

        for interval in intervals:
            if interval[1] < newInterval[0]:  
                result.append(interval)
            elif interval[0] > newInterval[1]:  
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            else:  
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not inserted:
            result.append(newInterval)

        return result