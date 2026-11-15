class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [j for j in board[i] if j!="."]
            if len(row)!=len(set(row)):
                return False
            
            col = [board[j][i] for j in range(9) if board[j][i]!="."]
            if len(col)!=len(set(col)):
                return False
            
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [
                    board[r + dr][c + dc]
                    for dr in range(3)
                    for dc in range(3)
                    if board[r + dr][c + dc] != "."
                ]
                if len(box) != len(set(box)):
                    return False
            

        return True

        