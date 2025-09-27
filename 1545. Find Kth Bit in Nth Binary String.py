# problem link-->> https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        invert = False
        while length > 1:
            mid = length // 2
            if k <= mid:
                length = mid

            elif k == mid+1:
                return "1" if not invert else '0'
            else:
                k = length - (k-1)
                length = mid
                invert = not invert
        return '0' if not invert else '1'
            
        
