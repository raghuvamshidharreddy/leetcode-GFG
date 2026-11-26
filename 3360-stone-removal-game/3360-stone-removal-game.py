class Solution:
    def canAliceWin(self, n: int) -> bool:
        isalice=True
        t=10
        while(n>=0):
            isalice =not isalice
            n-=t
            t-=1
        return isalice