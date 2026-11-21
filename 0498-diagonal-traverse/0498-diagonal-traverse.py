class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        dic={}
        for i in range(len(mat)+len(mat[0])-1):
            dic[i]=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in dic:
                    dic[i+j].append(mat[i][j])
                    print(mat[i][j],end=" ")
            print()
        ans=[]
        for i in dic.keys():
            if i%2==0:
                ans.extend(dic[i][::-1])
            else:
                ans.extend(dic[i])
        return ans
