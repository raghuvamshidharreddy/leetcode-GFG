class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        t=len(s)
        for i in range(len(s)):
            if s[i].isnumeric():
                stack.append(s[i])
                continue
            if s[i]=="]":
                t=''
                while(stack and stack[-1]!="["):
                    t+=stack.pop()[::-1]
                stack.pop()
                if not stack:
                    stack.append(t[::-1])
                else:
                    if stack and stack[-1].isnumeric():
                        num=''
                        while(stack and stack[-1].isnumeric()):
                            num+=stack.pop()
                        stack.append(int(num[::-1])*t[::-1])
                    else:
                        stack.append(stack.pop()+t[::-1])
                continue
            stack.append(s[i])
        print(stack)
        return ''.join(stack)

                