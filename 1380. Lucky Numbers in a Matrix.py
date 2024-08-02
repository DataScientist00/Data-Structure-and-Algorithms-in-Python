#problem link--->> https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        small , idx , large = 0 , 0 , 0
        res= []
        
        for i in range(len(matrix)):
            small = min(matrix[i])
            idx = matrix[i].index(small)
            for j in range(len(matrix)):
                large = max(large , matrix[j][idx])
            if large == small:
                res.append(small)
            large = 0
        return res


        
