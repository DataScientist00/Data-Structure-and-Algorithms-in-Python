#problem link-->> https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        mintime = []
        res = 0
        for d , s in zip(dist , speed):
            mintime.append(math.ceil(d / s))
        mintime.sort()
        for i in range(len(mintime)):
            if i >= mintime[i]:
                return res
            res += 1
        return res

        
