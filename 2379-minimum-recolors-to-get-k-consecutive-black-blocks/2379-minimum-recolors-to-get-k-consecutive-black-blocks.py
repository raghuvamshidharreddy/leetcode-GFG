class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        for i in range(k):
            if blocks[i]=='W':
                count+=1
        min_count=count
        j=0
        for i in range(k,len(blocks)):
            if blocks[j]=='W':
                count-=1
            if blocks[i]=='W':
                count+=1
            min_count=min(min_count,count)
            j+=1
        return min_count

