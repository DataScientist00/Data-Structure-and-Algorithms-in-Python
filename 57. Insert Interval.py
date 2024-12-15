#problem link-->> https://leetcode.com/problems/insert-interval/description/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        mid = 0
        for s , e in intervals:
            if s < newInterval[0]:
                output.append([s,e])
                mid += 1
            else:
                break
        
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1] , newInterval[1])
        
        for s , e in intervals[mid:]:
            if output[-1][1] < s:
                output.append([s,e])
            else:
                output[-1][1] = max(output[-1][1] , e)
        return output        
