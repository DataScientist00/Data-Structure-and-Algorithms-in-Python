# problem link-->> https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0,0,0]
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        if min(cnt) < k:
            return -1

        ans = -1
        l = 0
        for r in range(len(s)):
            cnt[ord(s[r]) - ord('a')] -= 1
            if min(cnt) < k:
                cnt[ord(s[l]) - ord('a')] += 1
                l += 1
            ans = max(ans , r-l+1)
        return len(s) - ans
        
