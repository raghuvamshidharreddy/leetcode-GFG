class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=[]
        for i,j in enumerate(number):
            if j==digit:
                l.append(i)
        print(l)
        ans=0
        for i in l:
            split1=number[:i] if number[:i] else ''
            split2=number[i+1:] if i+1<len(number) else ''
            print(split1,split2)
            ans=max(ans,int(str(split1)+str(split2)))
        return str(ans)