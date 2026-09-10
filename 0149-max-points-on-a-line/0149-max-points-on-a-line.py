class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans=0
        if len(points)==1:
            return 1
        for i in range(len(points)):
            xi=points[i][0]
            yi=points[i][1]
            dic={}
            for j in range(i+1,len(points)):
                xj=points[j][0]
                yj=points[j][1]
                if xi-xj==0:
                    dic['uk']=dic.get('uk',0)+1
                else:
                    slope=(yi-yj)/(xi-xj)
                    dic[slope]=dic.get(slope,0)+1
            print(dic)
            if dic:
                ans=max(ans,max(dic.values())) 
            print(ans)
        return ans+1