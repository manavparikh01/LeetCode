class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        arr = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            count = 1
            # temp = []
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                # temp.append(stack.pop())
                stack.pop()
            if len(stack) > 0:
                arr[i] = stack[-1] - i
            # while temp:
            #     stack.append(temp.pop())
            stack.append(i)
        return arr