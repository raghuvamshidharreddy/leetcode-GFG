class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52                         # 1..50 domain
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        cover = 0
        for x in range(1, 51):
            cover += diff[x]
            if left <= x <= right and cover == 0:
                return False
            if x == right:
                return True
        return True