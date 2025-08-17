class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        for i in range(len(hand) // groupSize):
            temp = float('inf')
            for j in range(groupSize):
                if len(hand) > 0 and temp == float('inf'):
                    temp = hand[0]
                    hand.remove(temp)
                elif len(hand) > 0 and temp + 1 in hand:
                    temp += 1
                    hand.remove(temp)
                else:
                    return False
        return True