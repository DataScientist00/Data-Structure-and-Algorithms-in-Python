#problem link-->> https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res , l , temp = 0 , 0 ,0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            if ((r- l + 1) - max(count.values())) <= k:
                res = max(res ,(r- l + 1))
            else:
                count[s[l]] -= 1
                l += 1
        return res

        
