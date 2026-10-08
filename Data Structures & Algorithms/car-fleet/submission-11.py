class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        queue = []
        for i in range(len(position)):
            queue.append((position[i], speed[i]))
        queue.sort()
        # print(queue)
        counter = 0
        prevTime = 0
        while queue:
            p, s = queue.pop()
            time = (target-p) / s
            if time > prevTime:
                counter += 1
                prevTime = time
                # print(p,s, time)
        return counter
            
            
            

