class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        t = s.strip()
        if not t:
            return 0
        sign = t[0]
        
        if sign == "-":
            sign = -1
            pos = 1
        elif sign == "+":
            sign = 1
            pos = 1
        else:
            sign = 1
            pos = 0
        
        res_list = []
    
        start = True
        while pos < len(t):
            while start and t[pos] == 0:
                pos += 1
                
            start = False
            if t[pos].isnumeric() == False:
                break
            res_list.append(t[pos])
            pos += 1
            
        res = 0
        print(res_list)
        for i in range(len(res_list)): 
            print(i)
            res += int(res_list[::-1][i]) * (10 ** i)
        print(res)
        res *= sign
        
        if res > 2**31 - 1:
            return 2**31 -1
        elif res < -(2**31):
            return -(2**31)
        return res