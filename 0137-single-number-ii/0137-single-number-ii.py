class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1
        for key,value in dic.items():
            if value==1:
                return key
        