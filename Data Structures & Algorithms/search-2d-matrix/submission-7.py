class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        finalRow = float("infinity")
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                finalRow = m
                break
        print(finalRow)
        if finalRow == float("infinity"):
            return False
        
        l = 0
        r = len(matrix[finalRow]) - 1
        arr = matrix[finalRow]

        while l <= r:
            m = (l + r) // 2
            if target > arr[m]:
                l = m + 1
            elif target < arr[m]:
                r = m - 1
            else:
                return True
        return False
