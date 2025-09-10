class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = 0
        r = 0
        freq = defaultdict(int)
        while r < len(paragraph):
            while r < len(paragraph) and paragraph[r].isalpha():
                r += 1
            word = paragraph[l:r]
            low = word.lower()
            if low not in banned:
                if low.isalpha():
                    freq[low] = freq[low] + 1
            l = r
            l += 1
            r += 1
        maxi = 0
        res = ""
        print(freq)
        for key, val in freq.items():
            if val > maxi:
                res = key
                maxi = val
        return res