class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            arr[i][len(word2)] = len(word1) - i
        for i in range(len(word2) + 1):
            arr[len(word1)][i] = len(word2) - i
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    arr[i][j] = arr[i + 1][j + 1]
                else:
                    arr[i][j] = 1 + min(arr[i + 1][j], arr[i + 1][j + 1], arr[i][j + 1])
        return arr[0][0]