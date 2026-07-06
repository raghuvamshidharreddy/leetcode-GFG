class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        arr=intervals.copy()
        res=[arr[0]]
        for i in range(1,len(intervals)):
            t=res[-1]
            c=arr[i]
            if t[0]==c[0]:
                if t[1]<c[1]:
                    t[1]=max(c[1],t[1])
            if t[1]>=c[1]:
                t[1]=max(c[1],t[1])
            else:
                res.append(c)
        return len(res)