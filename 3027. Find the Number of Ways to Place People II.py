# problem link-->> https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description/

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        for i in range(len(points)):
            _ , y1 = points[i]
            ymax = float('-inf')
            for j in range(i+1 , len(points)):
                _ , y2 = points[j]
                if y1 >= y2 and y2 > ymax:
                    count += 1
                    ymax = y2

        return count  

        
