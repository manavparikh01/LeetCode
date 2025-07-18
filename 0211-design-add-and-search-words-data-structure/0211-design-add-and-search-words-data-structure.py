class TrieNode() :

    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isLastLetter = True

    def search(self, word: str) -> bool:
        def dp(index, node):
            curr = node
        
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dp(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.isLastLetter
        return dp(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)