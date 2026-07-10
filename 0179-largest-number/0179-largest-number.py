from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            if x+y>y+x:
                return -1
            elif x+y<y+x:
                return 1
            else:
                return 0
        nums[:]=[str(i) for i in nums]
        sorted_nums=sorted(nums,key=cmp_to_key(compare))
        return "0" if all(i=='0' for i in sorted_nums) else ''.join(sorted_nums)
