class Solution:
    def mySqrt(self, x: int) -> int:
            start , end = 0 , x
            answer = 0
            while start <= end :
                mid = (start + end) // 2
                if mid ** 2 > x :
                    end = mid - 1
                elif mid ** 2 < x :
                    start = mid + 1
                    answer = mid
                else :
                    return mid

            return answer
        