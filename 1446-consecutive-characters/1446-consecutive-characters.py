class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        t=0
        while(t<len(s)):
            temp=t+1
            while(temp<len(s) and s[temp]==s[t]):
                temp+=1
            ans=max(ans,temp-t)
            t=temp
        ans=max(ans,temp-len(s))
        return ans