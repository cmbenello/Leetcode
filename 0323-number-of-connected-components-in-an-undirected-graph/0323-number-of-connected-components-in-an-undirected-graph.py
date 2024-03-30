class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set() 
        
        
        
        def dfs(a):
            connections = []
            visited.add(a)
            for x, y in edges:
                if x == a and y not in visited:
                    connections.append(y)
                if y == a and x not in visited:
                    connections.append(x)
            
            for con in connections:
                dfs(con)
                
        res = 0        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res