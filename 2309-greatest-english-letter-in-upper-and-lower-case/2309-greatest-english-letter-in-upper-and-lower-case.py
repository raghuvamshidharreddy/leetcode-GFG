class Solution:
    def greatestLetter(self, s: str) -> str:
        t=list(s)
        t=[i for i in s if i.isupper()]
        t=list(set(t))
        print(t)
        ans=set()
        for i in t:
            if i.lower() in s:
                ans.add(i)
        print(ans)
        ans=sorted(list(ans))
        print(ans)
        return ans[-1] if ans else ''
