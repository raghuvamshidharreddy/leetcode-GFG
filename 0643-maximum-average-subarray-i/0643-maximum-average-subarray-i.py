class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=0
        for i in range(k):
            ans+=nums[i]
        t=ans
        ans=ans/k
        for i in range(k,len(nums)):
            t=t-nums[i-k]+nums[i]
            ans=max(t/k,ans)
        return ans