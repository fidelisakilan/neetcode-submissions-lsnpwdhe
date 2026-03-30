class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        mid = 0
        result = None
        while(start <= end):
            mid = int((start + end) / 2)
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            if hours <= h:
                result = (mid, hours)
            if hours > h:
                start = mid + 1
            else:
                end = mid - 1

        return result[0]
                


