class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        shift = nums.index(0)

        def ring(k):
            return nums[(shift + k) % n]

        # Cyclically increasing
        if all(ring(k) == k for k in range(n)):
            return min(
                shift,          # rotate left shift times
                n - shift + 2  # reverse + rotate + reverse
            )

        # Cyclically decreasing
        if all(ring(k) == (-k) % n for k in range(n)):
            return min(
                shift + 2,  # rotate + reverse + reverse-equivalent path
                n - shift   # reverse first, then rotate
            )

        return -1