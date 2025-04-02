# problem link-->> https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in spells:
            left = 0
            right = len(potions) - 1
            idx = len(potions)
            while left <= right:
                mid = (left + right) // 2
                if i * potions[mid] >= success:
                    right = mid - 1
                    idx = mid
                else:
                    left = mid + 1
            res.append(len(potions)-idx)
        return res




        
