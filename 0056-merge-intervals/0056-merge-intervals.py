class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        length = len(intervals)
        
        i = 0
        
        while i < length - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                new_interval = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
                
                
                intervals.insert(i + 2, new_interval)
                intervals.pop(i)
                intervals.pop(i)       
                length -= 1

            else:
                i += 1
        
        return intervals