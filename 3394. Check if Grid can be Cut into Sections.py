#problem link-->> https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0] , r[2])for r in rectangles]
        y = [(r[1] , r[3])for r in rectangles]

        x.sort()
        y.sort()

        def countnonoverlapping(intervals):
            prev_end = -1
            count = 0
            for start , end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(end , prev_end)
            return count

        return max(countnonoverlapping(x) , countnonoverlapping(y)) >= 3
        
