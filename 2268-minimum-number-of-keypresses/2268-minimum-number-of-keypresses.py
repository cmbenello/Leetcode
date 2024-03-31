class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        
        i = 0
        res = 0
        
        temp = [val for key, val in count.items()]
        temp.sort()
        for value in temp[::-1]:
            res += value * ((i // 9) + 1)
            i += 1 
        
        return res
            