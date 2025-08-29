class DetectSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.point = []

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.point.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        res = 0
        for x, y in self.point:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            res += self.pointCount[(x, py)] * self.pointCount[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)