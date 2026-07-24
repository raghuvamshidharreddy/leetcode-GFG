from collections import deque
class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        def isSafe(x,y,n,m):
            if x>=n or y>=m or x<0 or y<0:
                return False
            return True
        q=deque()
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==2:
                    q.append((i,j))
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        elapsedTime=0
        while q:
            lenq=len(q)
            elapsedTime+=1
            for _ in range(lenq):
                i,j=q.popleft()
                for x, y in dir:
                    dx,dy=i+x,j+y
                    if isSafe(dx,dy,n,m) and mat[dx][dy]==1:
                        mat[dx][dy]=2
                        q.append((dx,dy))
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    return -1
        if elapsedTime==0:
            return 0
        else:
            return elapsedTime-1
            
