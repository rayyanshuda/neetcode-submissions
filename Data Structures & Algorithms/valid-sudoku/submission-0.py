class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need 3 diff helper functions
        # for row check, column check, and 3 square check

        # row check
        for row in board:
            seen_row = set()
            for number in row:
                if number == ".":
                    continue
                elif number in seen_row:
                    return False
                else:
                    seen_row.add(number)
        
        # column check
        i = 0
        while i < 9:
            seen_column = set()
            for row in board:
                if row[i] == ".":
                    continue
                elif row[i] in seen_column:
                    return False
                else:
                    seen_column.add(row[i])
            i += 1

        # 3x3 box check
        box_check = {}
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue
                elif (row//3, column//3) in box_check:
                    if board[row][column] in box_check[(row//3, column//3)]:
                        return False
                    else:
                        box_check[(row//3, column//3)].add(board[row][column])
                else:
                    # create a key
                    box_check[(row//3, column//3)] = set()
                    box_check[(row//3, column//3)].add(board[row][column])
        return True
                


        

        





