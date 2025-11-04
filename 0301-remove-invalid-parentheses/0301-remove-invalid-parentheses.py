class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        maxlength = -1
        res = set()
        def dp(curr_ind, curr_arr, l_val, r_val): #l_val = '(' r_val = ')'
            nonlocal s, maxlength, res
            if curr_ind >= len(s):
                if l_val == r_val:
                    if len(curr_arr) > maxlength:
                        maxlength = len(curr_arr)
                        res = set()
                        res.add("".join(curr_arr))
                    elif len(curr_arr) == maxlength:
                        res.add("".join(curr_arr))
                else:
                    return
                return
            curr_cha = s[curr_ind]
            if curr_cha == "(":
                curr_arr.append(curr_cha)
                dp(curr_ind + 1, curr_arr, l_val + 1, r_val)
                curr_arr.pop()
                dp(curr_ind + 1, curr_arr, l_val, r_val)
            elif curr_cha == ")":
                dp(curr_ind + 1, curr_arr, l_val, r_val)
                if l_val > r_val:
                    curr_arr.append(curr_cha)
                    dp(curr_ind + 1, curr_arr, l_val, r_val + 1)
                    curr_arr.pop()     
            else:
                curr_arr.append(curr_cha)
                dp(curr_ind + 1, curr_arr, l_val, r_val)
                curr_arr.pop()
        dp(0, [], 0, 0)
        return list(res)
            
