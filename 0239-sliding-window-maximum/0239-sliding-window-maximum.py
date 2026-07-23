from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()  # stores indices

        for i in range(len(nums)):
            # remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            # remove smaller values from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            # record max once window is full
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
