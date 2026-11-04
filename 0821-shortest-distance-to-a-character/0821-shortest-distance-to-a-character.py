class Solution:
    def shortestToChar(self, S, C):
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)
        return res