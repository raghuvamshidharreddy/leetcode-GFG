class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        numberTobeChanged = []

        for index, num in enumerate(nums):
            i = int(''.join(sorted(str(num), reverse=True)))

            if num < i:
                numberTobeChanged.append((i - num, i, index))

        numberTobeChanged.sort(reverse=True)

        while numberTobeChanged and k > 0:
            increase, num, index = numberTobeChanged.pop(0)
            nums[index] = num
            k -= 1

        return sum(nums)