class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        self.vo = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        def oneword(word):
            if word[0] in self.vo:
                return word + "ma"
            else:
                finw = word[1:] + word[0] + "ma"
                return finw
        i = 0
        res = []
        sen = sentence.split(" ")
        for word in sen:
            i += 1
            tranw = oneword(word)
            resa = ['a'] * i
            fins = tranw + "".join(resa)
            res.append(fins)
        return " ".join(res)