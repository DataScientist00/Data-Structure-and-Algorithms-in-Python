#problem link-->> https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for i in nums:
            if (i in count and i not in ans) and count[i] > 1:
                ans.append(i)
        return ans

        
