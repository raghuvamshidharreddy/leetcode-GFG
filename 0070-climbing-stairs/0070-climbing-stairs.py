class Solution:
    def climbStairs(self, n: int) -> int:
        b=1
        c=1
        if(n==1):
            return c
        else:
            while(n>1):
                d=b+c
                b=c
                c=d
                n-=1
        return d