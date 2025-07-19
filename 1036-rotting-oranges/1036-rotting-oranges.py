class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mainqueue = deque()
        time = 0
        totalfresh = 0

        def isfreshvalid(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 2 or grid[i][j] == 0:
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    mainqueue.append([i, j])
                if grid[i][j] == 1:
                    totalfresh += 1
        
        while mainqueue and totalfresh > 0:
            for i in range(len(mainqueue)):
                rotten = mainqueue.popleft()
                if isfreshvalid(rotten[0], rotten[1] + 1):
                    mainqueue.append([rotten[0], rotten[1] + 1])
                    grid[rotten[0]][rotten[1] + 1] = 2
                    totalfresh -= 1
                if isfreshvalid(rotten[0] + 1, rotten[1]):
                    mainqueue.append([rotten[0] + 1, rotten[1]])
                    grid[rotten[0] + 1][rotten[1]] = 2
                    totalfresh -= 1
                if isfreshvalid(rotten[0], rotten[1] - 1):
                    mainqueue.append([rotten[0], rotten[1] - 1])
                    grid[rotten[0]][rotten[1] - 1] = 2
                    totalfresh -= 1
                if isfreshvalid(rotten[0] - 1, rotten[1]):
                    mainqueue.append([rotten[0] - 1, rotten[1]])
                    grid[rotten[0] - 1][rotten[1]] = 2
                    totalfresh -= 1
            time += 1

        if totalfresh > 0:
            return -1
        return time