from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Helper function to compute the sum of digits
        def get_digit_sum(n: int) -> int:
            r = 0
            while n > 0:
                r += n % 10
                n //= 10
            return r

        n = len(nums)
        
        # 1. Create a list of tuples: (digit_sum, value, original_index)
        arr = []
        for i, val in enumerate(nums):
            arr.append((get_digit_sum(val), val, i))
            
        # 2. Sort based on the problem criteria:
        # First by digit sum, then by the value itself
        arr.sort(key=lambda x: (x[0], x[1]))
        
        # 3. Track visited elements to count permutation cycles
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct sorted position, skip
            if visited[i] or arr[i][2] == i:
                continue
                
            # Find the size of the current permutation cycle
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                # Move to the index where the element at current position came from
                j = arr[j][2]
                cycle_size += 1
                
            # A cycle of size K requires (K - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps
        