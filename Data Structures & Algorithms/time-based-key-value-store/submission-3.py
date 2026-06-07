class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.store[key]) - 1
        history = self.store[key]
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timestamp == history[mid][1]:
                return history[mid][0]
            elif timestamp > history[mid][1]:
                if history[mid][1] <= timestamp:
                    res = history[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
