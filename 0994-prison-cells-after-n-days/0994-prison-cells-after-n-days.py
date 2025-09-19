class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n

            if n >= 1:
                n -= 1
                arr = [0] * len(cells)
                for i in range(1, len(cells) - 1):
                    if cells[i - 1] == cells[i + 1]:
                        arr[i] = 1
                cells = arr.copy()
        return cells    
