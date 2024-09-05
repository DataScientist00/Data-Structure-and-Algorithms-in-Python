#problem link-->> https://leetcode.com/problems/find-unique-binary-string/description/


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        def backtrack(st):
            if len(st) == len(nums):
                if st not in nums:
                    res.append(st)
                    return
                return
            if len(res) > 0:
                return
            backtrack(st + '0')
            backtrack(st + '1')
        backtrack('')
        return res[0]
            


                  
