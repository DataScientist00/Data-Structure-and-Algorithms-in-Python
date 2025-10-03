# problem link-->> https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        table = [0] * 32
        for n in candidates:
            i = 0
            while n > 0:
                table[i] += 1 & n
                i += 1
                n = n >> 1
        return max(table)
        
            
            
        
