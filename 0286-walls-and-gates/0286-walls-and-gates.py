class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        q = deque()
        visit = set()
        
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r,c))
                    
        
        def addRooms(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or rooms[r][c] == -1 or (r, c) in visit:
                return
            q.append((r, c))
            visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            
            dist += 1
        
                
                
                
                
                