#problem link-->> https://leetcode.com/problems/permutation-difference-between-two-strings/description/


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index  = 0
        ans = 0
        for i in s:
            for j in range(len(t)):
                if i == t[j]:
                    ans += abs((index - j))
            index += 1
        return ans

        
