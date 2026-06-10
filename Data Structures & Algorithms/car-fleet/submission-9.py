class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for p, s in pairs:
            time = (target - p) / s
            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)
        print(stack)
        return len(stack)