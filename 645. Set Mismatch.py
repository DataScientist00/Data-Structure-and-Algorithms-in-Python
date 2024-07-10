#problem link-->> https://leetcode.com/problems/set-mismatch/description/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        count = Counter(nums)
        for i in range(len(nums)+1):
            if count[i] == 2:
                res[0]= i
            if count[i] == 0:
                res[1] = i
        return res
        
