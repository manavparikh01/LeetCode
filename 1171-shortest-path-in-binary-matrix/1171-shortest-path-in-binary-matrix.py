class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        if grid[0][0] or grid[ROW - 1][COL - 1] == 1:
            return -1
        queue = deque()
        queue.append((0, 0))
        length = 1
        visited = set()
        while queue:
            lenofnodes = len(queue)
            # print(lenofnodes)
            while lenofnodes > 0:
                i, j = queue.popleft()
                lenofnodes -= 1
                # print(i,j)
                if i < 0 or j < 0 or i == ROW or j == COL or grid[i][j] == 1 or (i, j) in visited:
                    continue
                visited.add((i ,j))
                if i == ROW - 1 and j == COL - 1:
                    return length
                queue.append((i + 1, j + 1))
                queue.append((i + 1, j))
                queue.append((i + 1, j - 1))
                queue.append((i, j - 1))
                queue.append((i - 1, j - 1))
                queue.append((i - 1, j))
                queue.append((i - 1, j + 1))
                queue.append((i, j + 1))
            length += 1
            # print(queue)
        return -1
                
        # ROW = len(grid)
        # COL = len(grid[0])
        # if grid[0][0] or grid[ROW - 1][COL - 1] == 1:
        #     return -1
        # arr = [[float("inf")] * (COL + 2) for i in range(ROW + 2)]
        # arr[ROW][COL] = 1
        # for ni in range(ROW - 1, -1, -1):
        #     for nj in range(COL - 1, -1, -1):
        #         if grid[ni][nj] == 1:
        #             continue
        #         i, j = ni + 1, nj + 1
        #         if arr[i][j] == 1:
        #             continue
        #         arr[i][j] = 1 + min(arr[i + 1][j + 1], arr[i + 1][j], arr[i + 1][j - 1], arr[i][j - 1], arr[i - 1][j - 1], arr[i - 1][j], arr[i - 1][j + 1], arr[i][j + 1])
        #         # if arr[i][j] == float("inf"):
        #         #     return -1
        # return arr[1][1] if arr[1][1] != float("inf") else -1