class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans=[['#' for i in range(n)] for j in range(m)]
        print(ans)
        for i in range(1):
            for j in range(n):
                ans[i][j]='.'
        print(ans)
        for i in range(1,m):
            for j in range(n):
                if j==n-1:
                    ans[i][j]='.'
        print(ans)
        return [''.join(i) for i in ans]