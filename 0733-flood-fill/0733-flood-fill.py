class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        ocolor = image[sr][sc]
        def dfs(i, j):
            nonlocal ocolor
            if i < 0 or j < 0 or i == len(image) or j == len(image[0]):
                return
            if (i, j) in visit:
                return
            if image[i][j] != ocolor:
                return
            visit.add((i, j))
            image[i][j] = color
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        dfs(sr, sc)
        return image