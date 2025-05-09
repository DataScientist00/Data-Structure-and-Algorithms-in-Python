# problem link-->> https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(i, j):
            # base 1
            if i == j:
                return 1

            # base 2
            if i > j:
                return 0

            # seen before
            if (i, j) in memo:
                return memo[(i, j)]

            # same character, change both pointers
            if s[i] == s[j]:
                memo[(i, j)] = 2 + dfs(i + 1, j - 1)
            else:
                # case 1; delete s[i]
                left = dfs(i + 1, j)

                # case 2; delete s[j]
                right = dfs(i, j - 1)

                # compare
                memo[(i, j)] = max(left, right)

            return memo[(i, j)]

        n = len(s)

        # memo[(i, j)] := maximum number of palindrome for s[i:j]
        memo = dict()

        return dfs(0, n - 1)
        
