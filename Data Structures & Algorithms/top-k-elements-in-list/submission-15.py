class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for i in range(0, len(nums)+1)]

        for num, count in counter.items():
            print(count, len(bucket))
            bucket[count].append(num)
        
        k_freq = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                k_freq.append(n)
                if len(k_freq) == k:
                    return k_freq
        return k_freq
            



        