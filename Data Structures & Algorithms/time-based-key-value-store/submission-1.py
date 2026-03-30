class TimeMap:

    def __init__(self):
        self.result = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.result[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.result[key]) - 1
        history = self.result[key]
        max_timestamp = None
        max_value = None
        while l <= r:
            mid = (l + r) // 2
            if timestamp == history[mid][1]:
                return history[mid][0]
            elif timestamp > history[mid][1]:
                if not max_timestamp or max_timestamp < history[mid][1]:
                    max_timestamp = history[mid][1]
                    max_value = history[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return max_value if max_value is not None else "" 
        
