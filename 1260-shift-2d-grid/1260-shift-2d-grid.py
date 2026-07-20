class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shifter(mat):
            m,n=len(mat)-1,len(mat[0])-1
            temp = [[0] * len(mat[0]) for _ in range(len(mat))]
            for i in range(len(mat)):
                for j in range(len(mat[i])-1):
                    temp[i][j+1]=mat[i][j]
            
            for i in range(len(mat)-1):
                temp[i+1][0]=mat[i][n]
            temp[0][0]=mat[m][n]
            mat[:]=temp
        n=len(grid)*len(grid[0])
        k=k%n
        for i in range(k):
            shifter(grid)
        return grid