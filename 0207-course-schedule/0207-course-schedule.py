class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        graph = {i : ([], []) for i in range(numCourses)}
        
        
        for course, prereq in prerequisites:
            graph[course][0].append(prereq)
            graph[prereq][1].append(course)
            
        
        q = deque()
        
        for course, prereqs in graph.items():
            if len(prereqs[0]) == 0:
                q.append((course, prereqs[1]))
        
        taken = set()
        while q:
            length = len(q) 
            for i in range(length):
                course, classes = q.popleft()
                taken.add(course)
                
                for c in classes:
                    graph[c][0].remove(course)
                    if len(graph[c][0]) == 0:
                        q.append((c, graph[c][1]))
                    
    
        return len(taken) == numCourses
                