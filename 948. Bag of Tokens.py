# problem link-- >> https://leetcode.com/problems/bag-of-tokens/description/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()
        l= 0
        r = len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res , score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return res

        
