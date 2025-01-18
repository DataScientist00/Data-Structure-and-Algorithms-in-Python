#problem link-->> https://leetcode.com/problems/hand-of-straights/description/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for c in hand:
            count[c] = 1 + count.get(c , 0)
        minh = list(count.keys())
        heapq.heapify(minh)
        while minh:
            first = minh[0]
            for i in range(first , first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minh[0]:
                        return False
                    heapq.heappop(minh)
        return True
        
        
