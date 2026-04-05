class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
        # k = len(nums) - k

        # def quickSelect(l, r):
        #     p = l
        #     for i in range(l, r):
        #         if nums[i] < nums[r]:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[r], nums[p] = nums[p], nums[r]
        #     if p > k: return quickSelect(l, p - 1)
        #     elif p < k: return quickSelect(p + 1, r)
        #     else: return nums[p]
        # return quickSelect(0, len(nums) - 1)


        