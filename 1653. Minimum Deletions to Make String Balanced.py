# problem link-->> https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix_b = defaultdict(int)
        suffix_a = defaultdict(int)
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'b':
                cnt += 1
                prefix_b[i] = cnt
            else:
                prefix_b[i] = cnt
        cnt = 0
        t = s[::-1]
        for i in range(len(t)):
            if t[i] == 'a':
                cnt += 1
                suffix_a[len(s)-i-1] = cnt
            else:
                suffix_a[len(s)-i-1] = cnt
        res = float('inf')
        for i in range(len(prefix_b)):
            res = min(res , prefix_b[i] + suffix_a[i])
        return res - 1

        
        

        
