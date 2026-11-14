class Solution:
    from collections import Counter
    uniqueOccurrences=lambda self, arr: all(i==1 for i in Counter(Counter(arr).values()).values())