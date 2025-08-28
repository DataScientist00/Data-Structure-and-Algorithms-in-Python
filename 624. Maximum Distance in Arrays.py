# problem link-->> https://leetcode.com/problems/maximum-distance-in-arrays/description/


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn ,maxx = arrays[0][0] , arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
            res = max(res , arrays[i][-1] - minn ,  maxx - arrays[i][0])
            minn = min(minn ,arrays[i][0])
            maxx = max(maxx,arrays[i][-1])
        return res


        
