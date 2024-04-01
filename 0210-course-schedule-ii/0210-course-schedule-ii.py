class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        # want to do a topolical sorting of it ykwim 
        
        res = [] 
        taken = set()
        
        graph = {i : ([],[]) for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            graph[course][0].append(prereq)
            graph[prereq][1].append(course)
            
        q = deque()
        
        for course, classes in graph.items():
            if len(classes[0]) == 0:
                q.append((course, classes[1]))
        
        while q:
            length = len(q)
            for i in range(length):
                curr, classes = q.popleft()
                if curr not in taken:
                    res.append(curr)
                    taken.add(curr)

                    for c in classes:
                        graph[c][0].remove(curr)
                        if len(graph[c][0]) == 0:
                            q.append([c, graph[c][1]])
        
        if len(res) != numCourses:
            return []
        else:
            return res