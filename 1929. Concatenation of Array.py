#problem link-->> class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans =  []
        ans = nums.copy()
        ans.extend(nums)
        return ans
        
