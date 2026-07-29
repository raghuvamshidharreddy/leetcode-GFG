class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri=[[1],[1,1]]
        if rowIndex>=2:
            for i in range(2,rowIndex+1):
                tri.append([1]*(i+1))
                for j in range(len(tri[i])):
                    if j==0 or j==i:
                        continue
                    tri[i][j]=tri[i-1][j]+tri[i-1][j-1]
        return tri[rowIndex]



