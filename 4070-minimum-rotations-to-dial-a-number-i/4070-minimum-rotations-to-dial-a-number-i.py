class Solution:
    def minRotations(self, s: str) -> int:
        ans=min(10-abs(int(s[0])),int(s[0]))
        for i in range(1,len(s)):
            n=int(s[i])
            p=int(s[i-1])
            ans+=min(10-abs(p-n),abs(p-n))
        return ans