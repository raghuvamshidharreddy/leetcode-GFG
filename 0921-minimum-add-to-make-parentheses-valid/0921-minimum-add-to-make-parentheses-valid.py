class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if i==")":
                if not stack:
                    stack.append(i)
                else:
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(i)
            else:
                stack.append(i)
            print(stack)
        print(stack)
        return len(stack)