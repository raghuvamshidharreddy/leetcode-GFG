from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # stop if out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # mark current cell as visited
            grid[r][c] = "0"
            # explore neighbors
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
