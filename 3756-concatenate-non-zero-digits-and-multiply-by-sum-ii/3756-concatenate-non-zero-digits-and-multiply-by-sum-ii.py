import sys
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        sys.set_int_max_str_digits(100000)
        MOD = 10**9 + 7
        n = len(s)

        # prefix sums of digits
        prefix_sum = [0] * (n + 1)
        # prefix modular values of non-zero digits
        prefix_val = [0] * (n + 1)
        # prefix count of non-zero digits
        prefix_len = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + int(s[i])
            if s[i] != '0':
                prefix_val[i+1] = (prefix_val[i] * 10 + int(s[i])) % MOD
                prefix_len[i+1] = prefix_len[i] + 1
            else:
                prefix_val[i+1] = prefix_val[i]
                prefix_len[i+1] = prefix_len[i]

        ans = []
        for start, end in queries:
            # sum of digits in range
            range_sum = prefix_sum[end+1] - prefix_sum[start]

            # number of non-zero digits in range
            length = prefix_len[end+1] - prefix_len[start]

            # value of substring modulo MOD
            # remove prefix contribution using modular inverse
            pow10 = pow(10, length, MOD)
            range_val = (prefix_val[end+1] - prefix_val[start] * pow10) % MOD

            ans.append((range_val * range_sum) % MOD)
        return ans
