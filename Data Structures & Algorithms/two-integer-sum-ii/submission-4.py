class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            sumof = numbers[p1] + numbers[p2]
            if sumof < target:
                p1 += 1
            elif sumof > target:
                p2 -= 1
            else:
                return [p1+1,p2+1]

