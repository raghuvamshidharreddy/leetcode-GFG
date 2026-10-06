class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        t=[i for i in range(mini,maxi+1)]
        set_diff=set(t)-set(nums)
        return sorted(list(set_diff))
        