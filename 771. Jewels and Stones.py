#problem link-->> https://leetcode.com/problems/jewels-and-stones/description/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(stones)
        ans = 0
        for i in jewels:
            if i in count:
                ans += count[i]
            count[i] = 0
        return ans
        
