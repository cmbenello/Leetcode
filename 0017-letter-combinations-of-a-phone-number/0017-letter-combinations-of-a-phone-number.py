class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2" : "abc",
                       "3" : "def",
                       "4" : "ghi",
                       "5" : "jkl",
                       "6" : "mno",
                       "7" : "pqrs",
                       "8" : "tuv",
                       "9" : "wxyz"}
        
        if digits == "":
            return []
        def dfs(digits, curr):
            if not digits:
                res.append(curr)
                return
            
            
            for char in digitToChar[digits[0]]:
                dfs(digits[1:], curr + char)
            
        dfs(digits,"")
        return res