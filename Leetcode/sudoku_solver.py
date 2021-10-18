SIZE = 9
SUB = 3

EMPTY = "."


class Solution:
    
    def solve_sudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(SIZE):
            
            for j in range(SIZE):
                
                if board[i][j] == EMPTY:
                    
                    for k in range(1, 10):

                        if self.is_valid(board, i, j, str(k)):
                            board[i][j] = str(k)

                            # backtrack
                            if not self.solve_sudoku(board):
                                board[i][j] = EMPTY

                            else:
                                return True

                    return False
            
        return True

                
                     
                
    def is_valid(self, board, x, y, num) -> bool:
        
        return self.valid_row(board, x, num) and self.valid_col(board, y, num) and self.valid_subgrid(board, x, y, num)
    
    
    
    def valid_row(self, board, x, num) -> bool:
        
        for i in range(SIZE):
            
            if board[x][i] == num:
                
                return False
            
        return True
    
    
    
    def valid_col(self, board, y, num) -> bool:
        
        for i in range(SIZE):
            
            if board[i][y] == num:
                
                return False
            
        return True
    
    
    
    
    def valid_subgrid(self, board, x, y, num) -> bool:
        
        lim_x = (x // SUB) * SUB
        lim_y = (y // SUB) * SUB
        
        for i in range(lim_x, lim_x + SUB):
            
            for j in range(lim_y, lim_y + SUB):
                
                if board[i][j] == num:
                    
                    return False
                    
        return True            