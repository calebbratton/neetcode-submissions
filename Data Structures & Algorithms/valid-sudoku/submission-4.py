class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        cellCheck = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = (i // 3) * 3 + (j // 3)
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in rowCheck[i]:
                    return False
                if curr in colCheck[j]:
                    return False
                if curr in cellCheck[cell]:
                    return False
                rowCheck[i].add(curr)
                colCheck[j].add(curr)
                cellCheck[cell].add(curr)
        return True
                