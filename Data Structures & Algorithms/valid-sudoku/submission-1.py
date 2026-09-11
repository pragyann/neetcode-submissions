class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        sq_map = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):

                if  board[i][j] in row_map[i] or \
                    board[j][i] in col_map[i] or \
                    board[i][j] in sq_map[tuple([i//3, j//3])]:
                    return False

                if board[i][j] != '.':
                    row_map[i].add(board[i][j])
                    sq_map[tuple([i//3, j//3])].add(board[i][j])
                if board[j][i] != '.':
                    col_map[i].add(board[j][i])
        

        
        return True
        