class Solution:
    def solveEquation(self, equation: str) -> str:
        lx = 0
        rx = 0
        lnum = 0
        rnum = 0
        nsign = False
        nrsign = False
        left, right = equation.split("=")
        i = 0
        j = 0
        while i < len(left):
            if left[i].isdigit():
                total = 0
                while i < len(left) and left[i].isdigit():
                    total = total * 10 + int(left[i])
                    i += 1
                if i < len(left) and left[i] == "x":
                    lx += total if nsign == False else -total
                else:
                    lnum += total if nsign == False else -total
                    i -= 1
            else:
                if left[i] == "x":
                    lx += 1 if nsign == False else -1
                elif left[i] == "-":
                    nsign = True
                else:
                    nsign = False
            i += 1
        while j < len(right):
            if right[j].isdigit():
                total = 0
                while j < len(right) and right[j].isdigit():
                    total = total * 10 + int(right[j])
                    j += 1
                if j < len(right) and right[j] == "x":
                    rx += total if nrsign == False else -total
                else:
                    rnum += total if nrsign == False else -total
                    j -= 1
            else:
                if right[j] == "x":
                    rx += 1 if nrsign == False else -1
                elif right[j] == "-":
                    nrsign = True
                else:
                    nrsign = False
            j += 1
        totx = lx - rx
        totnum = rnum - lnum
        if totx == 0 and totnum == 0:
            return "Infinite solutions"
        elif totx == 0 and totnum != 0:
            return "No solution"
        else:
            finnum = int(totnum / totx)
            return f"x={finnum}"
        # if (totx > 0 and totnum >= 0) or (totx < 0 and totnum <= 0):
        #     return f"{abs(totx)}x={abs(totnum)}"
        # return f"{abs(totx)}x=-{abs(totnum)}"