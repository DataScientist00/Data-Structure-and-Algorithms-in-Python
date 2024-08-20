#problem link-->> https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i , k in enumerate(temperatures):
            while stack and k > stack[-1][0]:
                temp , ind = stack.pop()
                res[ind] = i - ind
            stack.append((k,i))
        return res
        
