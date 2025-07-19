class TrieNode:

    def __init__(self):
        self.children = {}
        self.isLastLetter = False

    def insertWord(self, word):
        curr = self
        for character in word:
            if character not in curr.children:
                curr.children[character] = TrieNode()
            curr = curr.children[character]
        curr.isLastLetter = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        curr = TrieNode()
        temp = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for word in words:
            curr.insertWord(word)
        
        def dp(i, j, curr, templist):
            nonlocal res, temp
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or temp[i][j] == True or board[i][j] not in curr.children:
                return
            curr = curr.children[board[i][j]]
            templist += board[i][j]
            temp[i][j] = True
            if curr.isLastLetter == True:
                if templist not in res:
                    res.append(templist)
            dp(i, j + 1, curr, templist)
            dp(i + 1, j, curr, templist)
            dp(i, j - 1, curr, templist)
            dp(i - 1, j, curr, templist)
            temp[i][j] = False
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dp(i, j, curr, "")
        
        return list(res)