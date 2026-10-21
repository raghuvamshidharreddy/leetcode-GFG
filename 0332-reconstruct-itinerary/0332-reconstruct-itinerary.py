class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        dic = {}

        for i, j in tickets:
            if i not in dic:
                dic[i] = []
            dic[i].append(j)

        # sort destinations in reverse order
        for key in dic:
            dic[key].sort(reverse=True)

        ans = []

        def dfs(src):
            while src in dic and dic[src]:
                nxt = dic[src].pop()  # smallest lexicographic destination
                dfs(nxt)
            ans.append(src)

        dfs("JFK")

        return ans[::-1]