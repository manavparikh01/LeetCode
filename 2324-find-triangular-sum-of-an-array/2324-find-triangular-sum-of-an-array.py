class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        queue = deque()
        for num in nums:
            queue.append(num)
        while len(queue) > 1:
            length = len(queue)
            while length > 1:
                poped = queue.popleft()
                nxtpop = queue[0]
                sumi = (poped + nxtpop) % 10
                queue.append(sumi)
                length -= 1
            queue.popleft()
        return queue.popleft()
            