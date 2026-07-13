class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l,h=str(low),str(high)
        llen,hlen=len(l),len(h)
        s="123456789"
        ans=[]
        while((hlen-llen)>=0):
            for i in range(0,len(s)-llen+1):
                t=int(s[i:i+llen])
                if t>=low:
                    if t<=high:
                        ans.append(t)
                    else:
                        break
            llen+=1
        return ans


