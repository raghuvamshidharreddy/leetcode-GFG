from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(n):
            seive=[True]*(n+1)
            seive[0]=seive[1]=False
            for i in range(2,int(n**0.5)+1):
                if seive[i]:
                    for j in range(i*i,n+1,i):
                        seive[j]=False
            return sum(seive)
        noOfPrimes=countPrimes(n)
        nonPrimes=n-noOfPrimes
        return (factorial(noOfPrimes)*factorial(nonPrimes))%(10**9 +7)

