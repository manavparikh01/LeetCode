class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts2, counts1 = defaultdict(int), defaultdict(int)
        for c in s1:
            counts1[c] += 1
        have = 0
        need = len(counts1)
        l = 0
        print(need)
        for r in range(len(s2)):
            if s2[r] not in counts1:
                have = 0
                counts2 = defaultdict(int)
                l = r + 1
            else:
                counts2[s2[r]] += 1
                if counts2[s2[r]] == counts1[s2[r]]:
                    have += 1
                while counts2[s2[r]] > counts1[s2[r]]:
                    val = s2[l]
                    if counts2[val] == counts1[val]:
                        have -= 1
                    counts2[val] -= 1
                    l += 1
                # print(have, counts2)
                if have == need:
                    return True
        return False
            
