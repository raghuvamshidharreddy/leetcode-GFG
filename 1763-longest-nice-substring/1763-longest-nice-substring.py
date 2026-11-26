class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ''
        if len(s)==2 and (s[0]==s[1].upper() or s[0]==s[1].lower()):
            return s
        elif len(s)==2:
            return ''
        else:
            t=0
            ans=''
            for i in range(len(s)):
                temp=""
                temp1=0
                upper=set()
                lower=set()
                for j in range(i,len(s)):
                    temp+=s[j]
                    if s[j].isupper():
                        upper.add(s[j])
                    if s[j].islower():
                        lower.add(s[j])
                    print(lower,upper,temp)
                    if all(i.upper() in upper for i in lower) and all(i.lower() in lower for i in upper):
                        if t<len(temp):
                            t=len(temp)
                            ans=temp
            return ans if len(ans)>1 else ""
                        
                    

