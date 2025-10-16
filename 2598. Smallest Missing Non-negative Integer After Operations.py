# problem link-->> https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        num_set = defaultdict(int)
        for i in range(len(nums)):
            num_set[nums[i] % value] += 1

        MEX = 0
        while (MEX % value) in num_set and num_set[MEX % value] > 0:
            num_set[MEX % value] -= 1
            MEX += 1
        return MEX
            
        
