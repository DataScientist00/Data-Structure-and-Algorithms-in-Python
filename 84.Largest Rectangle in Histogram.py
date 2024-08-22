#problem link-->> https://leetcode.com/problems/largest-rectangle-in-histogram/description/



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxres = 0
        stack = []
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , val = stack.pop()
                maxres = max(maxres , val * (i-index))
                start = index
            stack.append((start,h))
        for i , h in stack:
            maxres = max(maxres , h * (len(heights)-i))
        return maxres
        
