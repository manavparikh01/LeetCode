class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        i = 0
        while i < len(path):
            string = ""
            if path[i] == "/":
                while i < len(path) and path[i] == "/":
                    string += path[i]
                    i += 1
            else:
                while i < len(path) and path[i] != "/":
                    string += path[i]
                    i += 1
            stack.append(string)
        newstack = []
        while stack:
            poped = stack.popleft()
            if poped == ".":
                if newstack:
                    newstack.pop()
            elif poped == "..":
                if newstack:
                    newstack.pop()
                if newstack:
                    newstack.pop()
                if newstack:
                    newstack.pop()
            else:
                if len(poped) > 1 and poped[0] == "/":
                    newstack.append("/")
                else:
                    newstack.append(poped)
        if newstack:
            if len(newstack) > 1 and newstack[-1] == "/":
                newstack.pop()
            return "".join(newstack)
        return "/"

        # while stack:
        #     temp = ""
        #     poped = stack.pop()
        #     print(tempstring, stack, poped)
        #     if poped == ".":
        #         if stack:
        #             stack.pop()
        #     elif poped == "..":
        #         if stack:
        #             stack.pop()
        #         if stack:
        #             stack.pop()
        #         if stack:
        #             stack.pop()
        #     else:
        #         if len(poped) > 1 and poped[0] == "/":
        #             temp = "/"
        #         else:
        #             temp = poped
        #     tempstring = temp + tempstring
        # if len(tempstring) > 1 and tempstring[-1] == "/":
        #     return tempstring[0:-1]
        # return tempstring