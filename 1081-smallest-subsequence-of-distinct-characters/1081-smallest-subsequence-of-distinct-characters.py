class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={ch:i for i,ch in enumerate(s)}
        seen=set()
        stack=[]
        for i,ch in enumerate(s):
            if ch in seen:
                continue
            while stack and ch<stack[-1] and i<last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)
