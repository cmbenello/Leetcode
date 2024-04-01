class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
        # check the click position and do cases 
        # If it is a mine just change to X and we are done
        
        def mine_nearby(x, y):
            count = 0
            for dx, dy in directions:
                if (y + dy in range(len(board)) and x + dx in range(len(board[0]))) and board[y + dy][x + dx] == "M": 
                    count += 1
            return count
            
        y, x = click
        val = board[y][x]
        
        if val == "M":
            board[y][x] = "X"
            return board
        
        if val == "E":
            # Check if there is a mine nearby - if there is then turn to digit and then go to next squares
            # if there is no mine nearby just go to the nearby squares
            
            if mine_nearby(x, y):
                board[y][x] = str(mine_nearby(x, y))
                return board
            else:
                board[y][x] = "B"
            
            for dx, dy in directions:
                new_y = y + dy
                new_x = x + dx
                if (new_y in range(len(board)) and new_x in range(len(board[0]))) and board[new_y][new_x] == "E":
                    board = self.updateBoard(board, [new_y, new_x])
            return board
            
