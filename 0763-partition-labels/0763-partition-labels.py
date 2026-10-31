class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        dic = {}
        for idx, ch in enumerate(s):
            dic[ch] = idx

        ans = []
        i = j = 0

        while j < len(s):

            end = dic[s[j]]

            while j < end:
                end = max(end, dic[s[j]])
                j += 1

            ans.append(j - i + 1)
            print(s[i:j + 1])

            j += 1
            i = j

        return ans