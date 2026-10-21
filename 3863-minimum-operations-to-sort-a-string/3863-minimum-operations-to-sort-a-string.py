class Solution:
    def minOperations(self, s: str) -> int:
        print(sorted(s))
        if s==''.join(sorted(s)):
            return 0
        if len(s)==2:
            return -1
        min_char=s[0]
        max_char=s[-1]
        for i in s:
            min_char=min(min_char,i)
            max_char=max(max_char,i)
        if min_char==s[0] or max_char==s[-1]:
            return 1
        elif max_char==s[0] and min_char==s[-1] and (s.count(max_char)==1 and s.count(min_char)==1):
            return 3
        else:
            return 2
