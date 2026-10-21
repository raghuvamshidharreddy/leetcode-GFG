class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        dic={}
        for i,j in tickets:
            if i not in dic:
                dic[i]=[]
            dic[i].append(j)
        print(dic)
        for i,j in dic.items():
            j.sort(reverse=True)
        print(dic)
        ans=[]
        def dfs(src):
            while src in dic and  dic[src] :
                c=dic[src].pop()
                dfs(c)
            ans.append(src)
        dfs("JFK")
        print(ans[::-1])
        return ans[::-1]
# class Solution:
#     def findItinerary(self, tickets: list[list[str]]) -> list[str]:
#         dic = {}

#         for i, j in tickets:
#             if i not in dic:
#                 dic[i] = []
#             dic[i].append(j)

#         # sort destinations in reverse order
#         for key in dic:
#             dic[key].sort(reverse=True)

#         ans = []

#         def dfs(src):
#             while src in dic and dic[src]:
#                 nxt = dic[src].pop()  # smallest lexicographic destination
#                 dfs(nxt)
#             ans.append(src)

#         dfs("JFK")

#         return ans[::-1]