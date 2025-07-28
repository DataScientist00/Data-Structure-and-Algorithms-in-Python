problem link-->> https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or = max_or | n

        def backtrack(idx , cur_or):
            if len(nums) == idx:
                if cur_or == max_or:
                    return 1
                else:
                    return 0

            if cur_or == max_or:
                return 2**(len(nums) - idx)

            return backtrack(idx+1 , nums[idx] | cur_or) + backtrack(idx + 1 , cur_or)


        return backtrack(0 , 0)        

