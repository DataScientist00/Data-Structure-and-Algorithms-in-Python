#problem link-->> https://leetcode.com/problems/permutations-ii/description/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        def dfs():
            if len(temp) == len(nums):
                res.append(temp[:])
                return

            for n in count:
                if count[n] > 0:
                    temp.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    temp.pop()
                
        dfs()
        return res
