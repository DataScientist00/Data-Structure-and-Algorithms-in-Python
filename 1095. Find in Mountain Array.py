# problem link-->> https://leetcode.com/problems/find-in-mountain-array/description/


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        N = mountainArr.length()
        l,r =0,N-1
        while l<r:
            mid = l + (r-l)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                l = mid+1
            else:
                r = mid
        peak = l
        l,r = 0, peak
        while l<=r:
            mid = l+(r-l)//2
            x = mountainArr.get(mid)
            if x==target:
                return mid
            elif x<target:
                l = mid+1
            else:
                r = mid-1
        l,r = peak+1, N-1
        while l<=r:
            mid = l+(r-l)//2
            x = mountainArr.get(mid)
            if x==target:
                return mid
            elif x>target:
                l = mid+1
            else:
                r = mid-1
        return -1
        
        
