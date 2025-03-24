#problem link-->>> https://leetcode.com/problems/count-days-without-meetings/description/


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = meetings[0][0] - 1
        last = meetings[0][-1]
        for start , end in meetings:
            if start > last:
                res += start-last-1
            last = max(last , end)
        res = res + days - last
        return res
        
