class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            size = 1

            for r in range(m):
                if grid[r][j] == 1 and (r, j) not in visited:
                    size += dfs(r, j)

            for c in range(n):
                if grid[i][c] == 1 and (i, c) not in visited:
                    size += dfs(i, c)

            return size

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = dfs(i, j)
                    if size > 1:
                        ans += size

        return ans