class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        dic={
            '{':'}',
            '[':']',
            '(':')'
        }
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack or dic[stack.pop()]!=i:
                    return False
        return len(stack)==0