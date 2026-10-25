class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        if all(i==0 for i in nums):
            return 0
        pref_sum=[0]*len(nums)
        pref_sum[0]=nums[0]
        for i in range(1,len(nums)):
            pref_sum[i]=pref_sum[i-1]+nums[i]
        print(pref_sum)
        n=len(nums)
        if pref_sum[-1]-pref_sum[0]==0:
            return 0
        for i in range(1,n):
            if pref_sum[-1]-pref_sum[i]==pref_sum[i-1]:
                return i
        if pref_sum[n-1]-nums[n-1]==0:
            return len(nums)-1
        return -1