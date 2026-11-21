class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum((i for i,j in Counter(nums).items() if j==1 ))