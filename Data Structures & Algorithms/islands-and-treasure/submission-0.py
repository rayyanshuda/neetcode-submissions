class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        # we can start from treasure chests, and move out from there
        # this is a bfs graph question
        # get rows and columns
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        # go through entire grid and find all treasures and add to a queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # found a treasure
                    q.append([r, c])

        # pseudo code
        
        # while there are elements inside the queue
        while q: 
            node = q.popleft()
            r, c = node[0], node[1]
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                
                # bounds & make sure the cell is an unvisited land cell
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr, nc])
            # how do i get the current element q's values

        return
            # start BFS -> in bfs, send grid and current distance to treasure (since we're at treasure -> d = 0)
        # return grid 

# edge cases
# 1. a grid with no treasures -> return the grid as is (no elements in queue)
# 2. if we only have treasures on this island -> should also just return the island as is
# 3. no water -> should not be an issue
# 4. all water and island -> should be a grid of -1 and 0's
# 5. if empty grid -> return grid