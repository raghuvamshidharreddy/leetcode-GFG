class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=len(arr1)
        for i in arr1:
            if any(abs(j-i)<=d for j in arr2):
                ans-=1
        return ans