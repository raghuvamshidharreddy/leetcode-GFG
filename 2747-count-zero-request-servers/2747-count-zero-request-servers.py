from collections import defaultdict
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        logs.sort(key=lambda log: log[1])

        q = [(val, idx) for idx, val in enumerate(queries)]
        q.sort()

        freq = defaultdict(int)
        active = 0

        left = 0
        right = 0

        ans = [0] * len(queries)

        for time, idx in q:

            # Add logs with timestamp <= time
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            # Remove logs with timestamp < time - x
            while left < len(logs) and logs[left][1] < time - x:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans

