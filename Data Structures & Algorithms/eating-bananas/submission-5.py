class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        mid = 0
        result = end
        while(start <= end):
            mid = (start + end) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            if hours <= h:
                result = mid
                end = mid - 1
            else:
                start = mid + 1

        return result
                


