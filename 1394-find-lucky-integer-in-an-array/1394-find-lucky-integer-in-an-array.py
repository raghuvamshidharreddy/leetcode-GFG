class Solution:
    def findLucky(self, arr: list[int]) -> int:
        from collections import Counter
        c=Counter(arr)
        s=sorted(list(Counter(arr).values()))[::-1]
        for i in s:
            if c[i]==i:
                return i
        return -1