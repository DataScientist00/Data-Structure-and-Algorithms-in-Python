#problem link-->> https://leetcode.com/problems/subsets/description/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(i):
            if i == len(nums):
                ans.append(temp.copy())
                return
            #Case when we select this index value
            temp.append(nums[i])
            dfs(i+1)

            #Case when we don't select this index value
            temp.pop()
            dfs(i+1)

        dfs(0)
        return ans

        
