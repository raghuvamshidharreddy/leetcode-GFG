class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li=[]
        for i in matrix:
            for j in i:
                li.append(j)
        li.sort()
        return li[k-1]