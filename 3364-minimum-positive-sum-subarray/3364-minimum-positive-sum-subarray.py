class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            t = 0

            for j in range(i, min(i + l, len(nums))):
                t += nums[j]

            if i + l <= len(nums) and t > 0:
                ans = min(ans, t)

            for k in range(i + l, min(i + r, len(nums))):
                t += nums[k]
                if t > 0:
                    ans = min(ans, t)

        return ans if ans != float('inf') else -1