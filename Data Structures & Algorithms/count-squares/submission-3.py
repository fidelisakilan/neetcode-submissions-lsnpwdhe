class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        squares = 0
        x, y = point
        for diag, count in self.points.items():
            dx,dy = diag
            if dx == x and dy == y:
                continue
            if abs(dx - x) != abs(dy - y):
                continue
            if (x,dy) in self.points and (dx, y) in self.points:
                squares += count * self.points[(x,dy)] * self.points[(dx,y)]
        return squares
        
