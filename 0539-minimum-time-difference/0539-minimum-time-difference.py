class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        import datetime

        for i in range(len(timePoints)):
            timePoints[i] = datetime.datetime.strptime(
                timePoints[i], "%H:%M"
            )

        timePoints.sort()

        ans = float('inf')

        for i in range(len(timePoints) - 1):
            diff = (timePoints[i + 1] - timePoints[i]).seconds // 60
            ans = min(ans, diff)

        # circular difference
        first = timePoints[0]
        last = timePoints[-1]

        circular = (
            (first + datetime.timedelta(days=1)) - last
        ).seconds // 60

        ans = min(ans, circular)

        return ans
