class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # go through k from 1 to max count
        # for each speed, get the hours and compares with result

        # for k in range(1, max(piles)+1):
        #     hours = 0
        #     for i in range(len(piles)):
        #         hours += math.ceil(piles[i]/k)    
        #     if hours <= h:
        #         return k
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)    
            if hours > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
            
        return res