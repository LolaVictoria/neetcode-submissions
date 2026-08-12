class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # One set per row (9 rows)
        rows_seen = [set() for _ in range(9)]

        # One set per col (9 cols)
        cols_seen = [set() for _ in range(9)]

        # One set per box (9 boxes)
        boxes_seen = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue  #skip empty cells
                val = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if val in rows_seen[r] or val in cols_seen[c] or val in boxes_seen[box_index]:
                    return False

                rows_seen[r].add(val)
                cols_seen[c].add(val)
                boxes_seen[box_index].add(val)
        return True
 
        
        