class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}

        for i in arr2:
            dic[i]=0
        l=[]
        for i in arr1:
            if i in dic:
                dic[i]=dic.get(i,0)+1
        for i in arr1:
            if i not in dic:
                l.append(i)
        print(dic)
        ans=[]
        for i,j in dic.items():
            ans.extend([i]*j)
        print(ans)
        ans[:]=ans+sorted(l)
        return ans