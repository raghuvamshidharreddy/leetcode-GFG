class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def length(mat):
            t=0
            for i in mat:
                t+=len(i)
            return t
        def reshape(mat):
            temp=[]
            for i in mat:
                for j in i:
                    temp.append(j)
            solved_mat=[[ 0 for _ in range(c)] for _ in range(r)]
            t=0
            for i in range(r):
                for j in range(c):
                    solved_mat[i][j]=temp[t]
                    t+=1
            return solved_mat
        if length(mat)<r*c or length(mat)>r*c:
            return mat
        else:
            t=reshape(mat)
            return t