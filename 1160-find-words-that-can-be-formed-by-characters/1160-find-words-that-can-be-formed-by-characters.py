class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        from collections import Counter
        ans=0
        for i in words:
            c=Counter(chars)
            t=0
            for j in i:
                if j not in c:
                    t=0
                    break
                else:
                    if c[j]==0:
                        t=0
                        break
                    else:
                        c[j]-=1
                        t+=1
            ans=ans+t
        return ans