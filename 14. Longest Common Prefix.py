# problem link-->> https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        if not strs:
            return ""

        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return ans
            ans += strs[0][j] 
        return ans
        
