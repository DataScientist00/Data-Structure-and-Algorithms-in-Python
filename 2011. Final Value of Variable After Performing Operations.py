#problem link-->> https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for t in operations:
            if t == "++X" or t == "X++":
                ans += 1
            else:
                ans -= 1
        return ans
        
