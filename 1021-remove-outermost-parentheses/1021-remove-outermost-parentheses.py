class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter=0
        l=[]
        t=""
        for i in s:
            if i=="(":
                counter+=1
                t+=i
            elif i==")" and counter>0:
                counter-=1
                t+=")"
            if counter==0:
                l.append(t)
                t=""
        for i in range(len(l)):
            l[i]=l[i][1:-1]
        return ''.join(l)
