#problem link-->> https://leetcode.com/problems/find-indices-of-stable-mountains/description/


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        num = 0
        for h in range(1,len(height)):
            num += 1
            if height[h-1] > threshold:
                res.append(num)
        return res 
        
