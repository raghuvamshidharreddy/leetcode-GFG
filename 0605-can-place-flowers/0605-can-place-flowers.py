class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        def isSafe(i):
            return i>=0 and i<len(flowerbed)
        if flowerbed.count(0)<n:
            return False
        placed=0
        for i in range(len(flowerbed)):
            if isSafe(i-1) and isSafe(i+1):
                if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    placed+=1
            if i-1==-1 and isSafe(i+1) and flowerbed[i+1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    placed+=1
            elif i+1==len(flowerbed) and flowerbed[i-1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                placed+=1
        print(placed)
        return placed>=n