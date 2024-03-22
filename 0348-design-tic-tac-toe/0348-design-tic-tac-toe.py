class TicTacToe:

    def __init__(self, n: int):
        self.hor_count = [0 for i in range(n)]
        self.vert_count = [0 for _ in range(n)]
        self.diag1 = 0
        self.diag2 = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            move = 1
        else:
            move = -1
            
        n = self.n
        
        self.hor_count[row] += 1 * move
        self.vert_count[col] += 1 * move
        
        if row == col:
            self.diag1 += 1 * move
        
        if row == self.n - 1 - col:
            self.diag2 += 1 * move
        
        if self.hor_count[row] == n or self.hor_count[row] == -n:
            return player
        
        if self.vert_count[col] == n or self.vert_count[col] == -n:
            return player 
        
        if self.diag1 == n or self.diag1 == -n:
            return player
        
        if self.diag2 == n or self.diag2 == -n:
            return player
        
        return 0
        
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)