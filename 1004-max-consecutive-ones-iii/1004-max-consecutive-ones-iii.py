class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero=0
        i,j=0,0
        ans=0
        while(j<len(nums)):
            if nums[j]==0:
                zero+=1
            if zero>k:
                ans=max(ans,j-i)
                while(i<len(nums) and zero>k):
                    if nums[i]==0:
                        zero-=1
                    i+=1
            j+=1
        return max(ans,j-i)
                    