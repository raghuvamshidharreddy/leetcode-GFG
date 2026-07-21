from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if reshape is possible
        if len(original) != m * n:
            return []
        
        # Build the 2D array
        t = [[0 for _ in range(n)] for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                t[i][j] = original[idx]
                idx += 1
        return t
