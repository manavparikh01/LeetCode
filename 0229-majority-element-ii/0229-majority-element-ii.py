class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = {}
        list = []
        length = len(nums)
        for i in nums:
            if i not in list:
                if i in map:
                    map[i] = map[i] + 1
                    if map[i] > length/3:
                        list.append(i)
                else:
                    map[i] = 1
                    if map[i] > length/3:
                        list.append(i)
        return list