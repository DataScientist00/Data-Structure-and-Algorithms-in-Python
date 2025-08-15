# problem link-->> https://leetcode.com/problems/sort-the-jumbled-numbers/description/


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i, n in enumerate(nums):
            mapp = 0
            n = str(n)
            for k in n:
                mapp = mapp * 10
                mapp += mapping[int(k)]

            pairs.append((mapp , i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]
        
