class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(i,j): set() for i in range(3)for j in range(3)}
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box = (r//3,c//3)
                
                if (val in rows[r] or val in cols[c] or val in boxes[box]):
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)
        return True
    
        