class Solution:
    
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        
        print(board)
        
        size = len(board)
        sub_size = size // 3
        
        for i in range(size):
            
            for j in range(size):
                
                val = board[i][j]
                
                if val == '.':
                    continue
                
                # check rows and columns
                for k in range(0, size):
                    if k != i and board[k][j] == val:
                        print('x')
                        return False
                    
                for k in range(0, size):
                    if k != j and board[i][k] == val:
                        print('x')
                        return False
                
                x = sub_size * (i // sub_size)
                y = sub_size * (j // sub_size)
                
                for m in range(x, x + sub_size):
                    for n in range(y, y + sub_size):
                        if (m != i or n != j) and board[m][n] == val:
                            print('y')
                            return False
                            
        return True