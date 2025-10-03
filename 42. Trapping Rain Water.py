 # problem link-->> https://leetcode.com/problems/trapping-rain-water/description/


class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        maxright = []
        temp = float('-inf')
        for h in height:
            temp = max(temp , h)
            maxleft.append(temp)
        temp = float('-inf')
        for h in reversed(height):
            temp = max(temp , h)
            maxright.append(temp)
        ans = 0
        i = 0
        j = len(height)-1
        for h in height:
            temp = min(maxleft[i] , maxright[j]) - h
            i += 1
            j -= 1
            if temp <= 0:
                continue
            ans += temp
        return ans
