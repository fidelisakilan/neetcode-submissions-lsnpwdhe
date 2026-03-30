class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        for p1, s1 in pair:
            t1 = (target - p1) / s1
            if stack:
                p2, s2 = stack[-1]
                t2 = (target - p2) / s2
                if t1 > t2:
                    stack.append((p1, s1))
            else:
                stack.append((p1, s1))
            print(stack)
        return len(stack)