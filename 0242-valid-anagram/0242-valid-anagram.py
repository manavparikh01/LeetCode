class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = defaultdict(int)
        for i in s:
            shash[i] += 1
        for j in t:
            if j not in shash:
                return False
            shash[j] -= 1
            if shash[j] == 0:
                del shash[j]
        return len(shash) == 0