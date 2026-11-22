class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        dic={}
        for  i in range(len(dominoes)):
            t=tuple(sorted(dominoes[i]))
            dic[t]=dic.get(t,0)+1
        ans=0
        for j in dic.values():
            ans+=j*(j-1)//2
        print(dic)
        return ans
