#problem link-->> https://leetcode.com/problems/subsets-ii/description/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res , temp = [] , []
        def backtrack(i):
            if i == len(nums):               
                res.append(temp[:])
                return
                         
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        backtrack(0)
        return res
        
