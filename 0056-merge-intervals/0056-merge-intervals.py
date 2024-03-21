class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[1])
        
        i = len(intervals) - 1
        
        while i > 0:
            if intervals[i][0] <= intervals[i - 1][1]:
                to_insert = [min(intervals[i][0], intervals[i - 1][0]), intervals[i][1]]
                intervals.insert(i + 1, to_insert)
                del intervals[i]
                del intervals[i - 1]
            i -= 1
            
        return intervals
            
        
        