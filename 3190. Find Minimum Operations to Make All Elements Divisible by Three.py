#problem link-->> https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s= 0
        for i in nums:
            if i % 3 == 0:
                pass
            else:
                s += 1
        return s
