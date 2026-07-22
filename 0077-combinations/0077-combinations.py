class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def sol(i, n, vis, k, t, res):
            if len(t) == k:
                res.append(t[:])   # append a copy
                return
            for j in range(i, len(n)):
                if not vis[j]:
                    vis[j] = True
                    t.append(n[j])
                    sol(j+1, n, vis, k, t, res)
                    t.pop()        # backtrack
                    vis[j] = False
            
        res=[]
        n=[i for i in range(1,n+1)]
        vis=[False]*len(n)
        sol(0,n,vis,k,[],res)
        return res
