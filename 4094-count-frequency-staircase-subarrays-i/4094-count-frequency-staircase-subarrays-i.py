class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        '''
        we want to find the sum of staircases in nums
        staircases for distint number in 1, 22, 333 ...

        we can do this in n^2 by running a sliding window and checking validity
        length of nums is 1500 so this is a plausible solution

        for every pass at i, consider if we have broken the sequence
        a, bb, ccc ... if we have then we can go the the next i
        loop for all i and total the valid seqs
        '''
        n = len(nums)
        res = 0
        for i in range(n):
            cnt = {}
            target = 1
            k = 1
            for j in range(i,n):
                num = nums[j]
                if num not in cnt:
                    cnt[num] = [1, target]
                    target += 1
                else:
                    cnt[num][0] += 1
                    
                if cnt[num][0] > cnt[num][1]:
                    break

                if j-i+1 == k * (k+1) // 2:
                    if all(count == target for count, target in cnt.values()):
                        res += 1
                    k += 1
        return res
                    
                