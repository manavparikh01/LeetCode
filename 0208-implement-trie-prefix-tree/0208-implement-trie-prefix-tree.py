class TrieNode:

    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for character in word:
            if character not in curr.children:
                curr.children[character] = TrieNode()
            curr = curr.children[character]
        curr.isLastLetter = True

    def search(self, word: str) -> bool:
        curr = self.root
        for character in word:
            if character not in curr.children:
                return False
            curr = curr.children[character]
        return curr.isLastLetter

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for character in prefix:
            if character not in curr.children:
                return False
            curr = curr.children[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)