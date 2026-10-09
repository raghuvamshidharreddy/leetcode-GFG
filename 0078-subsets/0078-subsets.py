class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        n=len(nums)
        for i in range(1,2**n):
            t=bin(i)[2::].zfill(n)
            one_index=[i for i in range(len(t)) if t[i]=='1']
            ans.append([nums[i] for i in one_index])
        return ans