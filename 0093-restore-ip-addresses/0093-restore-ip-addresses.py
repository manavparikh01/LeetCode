class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        arr = []
        temp = []
        def dfs(i, s):
            nonlocal arr, temp
            if len(temp) > 0:
                if int(temp[-1]) > 255:
                    return
            if len(temp) == 4 and i == len(s):
                arr.append(".".join(temp))
            if len(temp) == 4 and i < len(s):
                return
            if i >= len(s):
                return
            ip = s[i]
            temp.append(ip)
            dfs(i + 1, s)
            temp.pop()
            if s[i] != "0":
                if i + 1 < len(s):
                    ip = s[i:i+2]
                    temp.append(ip)
                    dfs(i + 2, s)
                    temp.pop()
                if i + 2 < len(s):
                    ip = s[i:i+3]
                    temp.append(ip)
                    dfs(i + 3, s)
                    temp.pop()
        dfs(0, s)
        return arr