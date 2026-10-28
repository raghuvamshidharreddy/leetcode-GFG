class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:(x[1],x[0]),reverse=True)
        print(boxTypes)
        i=0
        ans=0
        while(truckSize>0 and i<len(boxTypes)):
            t=boxTypes[i]
            box=t[0]
            units=t[1]
            if truckSize-box>=0:
                ans+=box*units
                truckSize-=box
                i+=1
            else:
                ans+=truckSize*units
                truckSize=0
        print(ans)
        return ans