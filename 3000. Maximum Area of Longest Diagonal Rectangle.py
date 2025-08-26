# problem link-->> https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        def diag(l , b):
            return (l**2 + b**2) ** 0.5
        diagonal = -1
        d= 0
        for i in dimensions:
            d =diag(i[0],i[1])
            if d == diagonal:
                if area < i[0] * i[1]:
                    area = i[0] * i[1]
                    diagonal = d
            elif d > diagonal:
                diagonal = d
                area = i[0] * i[1]
        return area


        
