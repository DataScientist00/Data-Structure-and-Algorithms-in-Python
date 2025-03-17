#problem link-->> https://leetcode.com/problems/divide-array-into-equal-pairs/description/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for count in counter.values():
            if count % 2 != 0:
                return False
        return True

        
