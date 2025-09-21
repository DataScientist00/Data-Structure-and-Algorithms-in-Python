# problem link-->> https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i , j in intervals:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        i = 0
        j = 0
        group = 0
        res = float('-inf')
        while i < len(start):
            if start[i] <= end[j]:
                group += 1
                i += 1
            else:
                group -= 1
                j +=1 
            res = max(res , group)
        return res

        
