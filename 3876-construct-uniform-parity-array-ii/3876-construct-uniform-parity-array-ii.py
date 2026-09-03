"""
ooe->
eeo->
ooo->
EEE->

"""
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd=float('inf')
        for i in nums1:
            if i&1==1:
                min_odd=min(min_odd,i)
        def parity_check(parity):
            for i in nums1:
                if((i&1)!=parity and i<=min_odd):
                    return False
            return True
        return parity_check(0)or parity_check(1)       