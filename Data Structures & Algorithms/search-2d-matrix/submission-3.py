class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s1, e1 = 0, len(matrix) - 1

        while s1 <= e1:
            mid1 = int((s1 + e1) / 2)
            first, last = matrix[mid1][0], matrix[mid1][-1]
            if first <= target <= last:
                s2, e2 = 0, len(matrix[0]) - 1
                while s2 <= e2:
                    mid2 = int((s2 + e2) / 2)
                    if matrix[mid1][mid2] == target:
                        return True
                    elif target < matrix[mid1][mid2]:
                        e2 = mid2 - 1
                    elif target > matrix[mid1][mid2]:
                        s2 = mid2 + 1
                return False
            elif target < first:
                e1 = mid1 - 1
            elif target > last:
                s1 = mid1 + 1
        return False
                

        