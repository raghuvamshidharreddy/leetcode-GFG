class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n

        s = set()
        for i in range(n):
            s.add(nums[i])
            pre[i] = len(s)

        s = set()
        for i in range(n - 2, -1, -1):
            s.add(nums[i + 1])
            suf[i] = len(s)

        ans = []
        for i in range(n):
            ans.append(pre[i] - suf[i])

        return ans