class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        seen = set()
        dic = {}

        for i in range(len(paths)):
            k, j = paths[i]
            dic[k] = j

        def dfs(place):
            if place not in dic:
                return place

            return dfs(dic[place])

        return dfs(paths[0][0])