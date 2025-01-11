#problem link-->> https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counter = defaultdict(int)
        res = 0
        for w ,h in rectangles:
            ratio = w /h
            res += counter.get(ratio , 0)
            counter[ratio] += 1
        return res
        
