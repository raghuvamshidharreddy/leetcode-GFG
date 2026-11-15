class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        mat = [[0] * n for _ in range(m)]

        for i, j in indices:
            # increment row i
            for c in range(n):
                mat[i][c] += 1

            # increment column j
            for r in range(m):
                mat[r][j] += 1

        cnt = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] % 2:
                    cnt += 1

        return cnt