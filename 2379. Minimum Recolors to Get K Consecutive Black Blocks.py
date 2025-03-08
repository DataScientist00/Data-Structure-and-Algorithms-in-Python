#problem link-->> https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = k
        temp = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                temp += 1
            if r - l + 1 == k:
                res = min(res , temp)
                if blocks[l] == 'W':
                    temp -= 1
                l += 1
        return res

        
