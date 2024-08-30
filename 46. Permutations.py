#problem link-->> https://leetcode.com/problems/permutations/description/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp , res = [] , []
        def dfs():
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs()
                    temp.pop()
        dfs()
        return res
        
