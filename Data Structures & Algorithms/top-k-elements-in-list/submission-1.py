from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        for value in nums:
            count[value] = 1 + count.get(value, 0)
        for num, c in count.items():
            count_bucket[c].append(num)
        result = []
        for index in range(len(count_bucket) - 1, 0, -1):
            for num in count_bucket[index]:
                result.append(num)
                if len(result) == k:
                    return result


                

        

