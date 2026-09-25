class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            total = numbers[l] + numbers[r]
            if total > target:
                r = r - 1
            elif total < target:
                l = l + 1
            else:
                return [l+1, r+1]