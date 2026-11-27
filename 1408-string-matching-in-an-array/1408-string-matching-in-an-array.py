class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        big_count=" ".join(words)
        res=[]
        for c in words:
            if big_count.count(c)>1:
                res.append(c)
        return res