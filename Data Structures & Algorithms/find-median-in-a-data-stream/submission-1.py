class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.right and (-self.left[0]) > self.right[0]:
            popped = -heapq.heappop(self.left)
            heapq.heappush(self.right, popped)
            diff = len(self.left) - len(self.right)
            
        diff = len(self.left) - len(self.right)
        if diff > 1:
            popped = -heapq.heappop(self.left)
            heapq.heappush(self.right, popped)
        if diff < -1:
            popped = heapq.heappop(self.right)
            heapq.heappush(self.left, -popped)
        
        print(self.left, self.right)
        

    def findMedian(self) -> float:
        diff = len(self.left) - len(self.right)
        if diff == 0:
            return (-self.left[0] + self.right[0]) / 2
        elif diff == -1:
            return self.right[0]
        else:
            return -self.left[0]


        
        