class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck, colCheck, cellCheck = defaultdict(set),defaultdict(set),defaultdict(set)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                cell = (r // 3) * 3 + (c // 3)
                print(cell)
                if value == ".":
                    continue
                if value in rowCheck[r] or value in colCheck[c] or value in cellCheck[cell]:
                    return False
                rowCheck[r].add(value)
                colCheck[c].add(value)
                cellCheck[cell].add(value)
                
        return True