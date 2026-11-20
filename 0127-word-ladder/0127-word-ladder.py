class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        hashmap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                hashmap[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                visited.add(word)
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    slist = hashmap[pattern]
                    for sword in slist:
                        if sword not in visited:
                            q.append(sword)
            res += 1
        return 0
