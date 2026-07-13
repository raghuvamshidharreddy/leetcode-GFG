class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        n=len(nums)
        for i in range(1,2**n):
            binary=bin(i)[2::].zfill(n)
            l=[i for i in range(len(binary)) if binary[i]=="1"]
            t=[nums[i] for i in l]
            t.sort()
            if t not in res:
                res.append(t)
        return res