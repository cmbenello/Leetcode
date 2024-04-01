class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # you are just doing offset from your starting value, so need to find the minimum value that you achieve, wlog can assume that you start at 0 and then update your lower based on the lower val found in the list, can do the same for upper and then your result is giong to be min(upper - max, min - lower)
        
        
        curr = 0
        

        min_val = curr
        max_val = curr
        
        for diff in differences:
            curr += diff
            
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)
        
        
        return max(upper - lower - (max_val - min_val) + 1, 0)
    
    # val 1 -2 2
    # min val 1 -2 
    # max val 1  1 2
    # res = min(6 - 4, 1 - 2 )
    
    # max_val = x
    # min_val = y
    
    
    # I know that numbers have a range of a and I the given range is b, so the possible combos is b - a
    # need x >=  lower and y <= upper
    # know that y - x = k  upper - x + lower - y