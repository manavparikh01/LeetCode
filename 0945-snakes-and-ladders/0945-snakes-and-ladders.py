class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def squaretorc(value):
            r = (value - 1) // length
            c = (value - 1) % length
            if r % 2 != 0:
                c = length - 1 - c
            return [r, c]
        queue = deque()
        queue.append([1, 0])
        visit = set()
        while queue:
            square, turn = queue.popleft()
            for i in range(1, 7):
                nextsquare = square + i
                r, c = squaretorc(nextsquare)
                if board[r][c] != -1:
                    nextsquare = board[r][c]
                if nextsquare == length * length:
                    return turn + 1
                if nextsquare not in visit:
                    visit.add(nextsquare)
                    queue.append([nextsquare, turn + 1])
        return -1