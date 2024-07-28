#problem link--->>>> https://leetcode.com/problems/height-checker/description/


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = heights.copy()
        a.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != a[i]:
                count += 1
        return count

        
