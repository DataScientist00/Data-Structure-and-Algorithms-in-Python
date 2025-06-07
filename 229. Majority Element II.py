# problem link-->> https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        x = len(nums) /3
        ans = []
        for i , cnt in count.items():
            if cnt > x:
                ans.append(i)
        return ans
        
