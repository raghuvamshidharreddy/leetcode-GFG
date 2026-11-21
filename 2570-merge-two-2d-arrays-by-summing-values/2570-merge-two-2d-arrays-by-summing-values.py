class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans=[]
        n={}
        for i,j in nums1:
            n[i]=j
        for i,j in nums2:
            if i not in n:
                ans.append([i,j])
            else:
                ans.append([i,n[i]+j])
                del n[i]
        for i in n.keys():
            ans.append([i,n[i]])
        ans.sort(key=lambda x:x[0])
        return ans
                
        