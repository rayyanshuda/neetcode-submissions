class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            # winning case:
            if i == len(word): 
                return True
            
            # failure cases
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#" # marking as visited

            found = (dfs(r + 1, c, i + 1) or # down
                    dfs(r - 1, c, i + 1) or # up
                    dfs(r, c + 1, i + 1) or # right
                    dfs(r, c - 1, i + 1)) # left

            board[r][c] = temp # return to normal

            return found

        ROWS = len(board)
        COLS = len(board[0]) 
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
