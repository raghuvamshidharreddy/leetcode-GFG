class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n=len(candidates)
        ans=[]
        def rec(num,target,arr,idx):
            if num==target:
                ans.append(arr.copy())
                return 
            if num>target:
                return 
            if idx==n:
                return
            arr.append(candidates[idx])
            rec(num+candidates[idx],target,arr,idx)
            arr.pop()
            rec(num,target,arr,idx+1)
        rec(0,target,[],0)
        return ans
        

                