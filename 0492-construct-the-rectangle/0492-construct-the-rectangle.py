class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        ans=[float('inf'),float('-inf')]
        temp=[]
        for w in range(1,int(area**0.5)+1):
            if area%w==0:
                l=area//w
                temp=[l,w]
                if (ans[0]-ans[1])>temp[0]-temp[1] and (temp[0]-temp[1]>=0):
                    ans=temp
        return ans

