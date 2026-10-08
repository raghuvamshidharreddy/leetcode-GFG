class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter=0
        l=[]
        ans=""
        t=""
        for i in s:
            if i=="(":
                counter+=1
                t+=i
            elif i==")" and counter>0:
                counter-=1
                t+=")"
            if counter==0:
                ans+=t[1:-1]
                t=""
        return ans
