class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        arr = []
        for key,val in hashmap.items():
            arr.append((val, key))
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        


        