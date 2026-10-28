class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans = 0

        while any(i != 0 for i in nums):
            min_number = min(i for i in nums if i > 0)

            for j in range(len(nums)):
                if nums[j] > 0:
                    nums[j] -= min_number

            ans += 1

        return ans