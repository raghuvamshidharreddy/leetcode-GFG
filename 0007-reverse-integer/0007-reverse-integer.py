class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        b = 2**31  # Representing the 32-bit boundary

        # Check for zero early
        if x == 0:
            return 0

        # Handle the negative case
        is_negative = x < 0
        if is_negative:
            x = -x  # Make x positive for processing

        # Reverse the digits of x
        while x > 0:
            a = a * 10 + x % 10
            x //= 10

        # Restore negative sign if needed
        if is_negative:
            a = -a

        # Check for 32-bit overflow
        if a < -b or a > b - 1:
            return 0

        return a