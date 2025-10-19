
# problem link-->> https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        for r in matrix:
            rowkey = tuple(r)
            if r[0]:
                rowkey = tuple([0 if i else 1 for i in r])
            count[rowkey] += 1
        return max(count.values())
        
