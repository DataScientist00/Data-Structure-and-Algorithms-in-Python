# problem link-->> https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        freq_set = set()
        ans = 0
        for item , freq in count.items():
            while freq > 0 and freq in freq_set:
                freq -= 1
                ans += 1
            freq_set.add(freq)
        return ans
        
