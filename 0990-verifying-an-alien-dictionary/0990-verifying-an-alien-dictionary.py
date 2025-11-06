class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordi = {}
        for i in range(len(order)):
            ordi[order[i]] = i
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w2[j] != w1[j]:
                    print(w1[j], w2[j], ordi[w1[j]], ordi[w2[j]])
                    if ordi[w1[j]] > ordi[w2[j]]:
                        return False
                    break
        return True
