# problem link-->> https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        sortedCount = sorted(count.items(), key=lambda x: x[1],reverse=True)
        mul = 1
        res = 0
        t= 1
        for i , j in sortedCount:
            res += j * mul
            if t % 8 == 0:
                mul += 1
            t += 1
        return res
        
