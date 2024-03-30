class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i : [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        seen = set()
        
        def dfs(source, prev):
            if source in seen:
                return False
            
            seen.add(source)
            for nei in graph[source]:
                if nei == prev:
                    continue
                if not dfs(nei, source):
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n
            
            