class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]
        # if n <= 1:
        #     return 1

        # res = 0
        # for i in range(1, n + 1):
        #     res += self.numTrees(i - 1) * self.numTrees(n - i)

        # return res