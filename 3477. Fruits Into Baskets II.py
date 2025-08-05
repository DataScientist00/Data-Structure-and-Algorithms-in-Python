# problem link-->> https://leetcode.com/problems/fruits-into-baskets-ii/description/

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for i in range(len(fruits)):
            j = 0
            while j <= len(baskets) - 1:
                if fruits[i] <= baskets[j] and baskets[j] != 0:
                    baskets[j] = 0
                    fruits[i] = 0
                    break
                j += 1
            if fruits[i] != 0:
                res += 1
        return res
        
