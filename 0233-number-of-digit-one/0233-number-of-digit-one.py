class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        factor = 1
        while factor <= n:
            lower = n % factor
            curr = (n // factor) % 10
            higher = n // (factor * 10)

            if curr == 0:
                ans += higher * factor
            elif curr == 1:
                ans += higher * factor + lower + 1
            else:
                ans += (higher + 1) * factor

            factor *= 10
        return ans
