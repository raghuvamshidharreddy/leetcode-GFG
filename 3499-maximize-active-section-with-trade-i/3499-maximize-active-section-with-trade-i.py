class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        contarr = []
        n = len(s)
        cnt = 0

        # Step 1: Build contiguous run array (convert '1' → +, '0' → -)
        for i in range(n):
            if i != 0 and s[i] != s[i-1]:
                contarr.append(cnt)
                cnt = 0
            cnt = cnt + 1 if s[i] == '1' else cnt - 1
        contarr.append(cnt)

        # Step 2: Count total positives (all active sections)
        possum = sum(x for x in contarr if x > 0)

        # Step 3: Default answer = total ones (no trade)
        maxsum = possum

        # Step 4: Try trades: look for [-ve, +ve, -ve] pattern
        m = len(contarr)
        for i in range(1, m-1):
            if contarr[i] > 0 and contarr[i-1] < 0 and contarr[i+1] < 0:
                # Remove this +ve block, flip surrounding -ve blocks
                maxsum = max(maxsum, possum + abs(contarr[i-1] + contarr[i+1]))

        return maxsum
