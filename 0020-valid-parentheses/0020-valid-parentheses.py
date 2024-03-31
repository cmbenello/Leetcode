class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        b_map = {"}": "{", ")" : "(", "]" : "["}
        
        for i in s:
            if stack and i in b_map:
                if stack[-1] == b_map[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack) == 0