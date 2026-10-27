class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def isvalid(i,j):
            return i>=0 and i<len(grid) and j>=0 and j<len(grid[0])
        dir=[[-1,0],[1,0],[0,1],[0,-1]]
        perimeter=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=0
                    for k,l in dir:
                        if isvalid(i+k,j+l):
                            if grid[i+k][j+l]==1:
                                count+=1
                    if count==4:
                        perimeter+=0
                    elif count==3:
                        perimeter+=1
                    elif count==2:
                        perimeter+=2
                    elif count==1:
                        perimeter+=3
                    else:
                        perimeter+=4
                else:
                    continue
        return perimeter
                    