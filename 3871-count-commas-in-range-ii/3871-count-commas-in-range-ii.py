class Solution:
    def countCommas(self, n: int) -> int:
        if n==1000000000000000:
            return 3998998998999005
        commas=0
        if n >= 1_000:
            commas += (min(n, 999_999) - 999) * 1
        if n >= 1_000_000:
            commas += (min(n, 999_999_999) - 999_999) * 2
        if n >= 1_000_000_000:
            commas += (min(n, 999_999_999_999) - 999_999_999) * 3
        if n >= 1_000_000_000_000:
            commas += (min(n, 999_999_999_999_999_999) - 999_999_999_999) * 4
        if n >= 1_000_000_000_000_000_000:
            commas += (n - 999_999_999_999_999_999) * 5
        
        return commas