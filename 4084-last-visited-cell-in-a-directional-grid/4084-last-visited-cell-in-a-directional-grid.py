class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        dic = {
            "R": [0, 1],
            "L": [0, -1],
            "U": [-1, 0],
            "D": [1, 0]
        }

        temp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        temp[0][0] = 1

        ans = [0, 0]

        while True:
            i, j = ans
            t = dic[grid[i][j]]

            te = [ans[0] + t[0], ans[1] + t[1]]

            if (te[0] < 0 or te[0] >= len(grid) or
                te[1] < 0 or te[1] >= len(grid[0]) or
                temp[te[0]][te[1]] == 1):
                return ans

            ans = te
            temp[te[0]][te[1]] = 1
