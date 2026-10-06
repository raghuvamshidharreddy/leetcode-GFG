class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        l=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    l[i]=max(l[i],l[j]+1)
        return max(l)