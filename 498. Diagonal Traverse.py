# problem link-->> https://leetcode.com/problems/diagonal-traverse/description/


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        mapping = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mapping[i+j].append(mat[i][j])
        for i in range(len(mapping)):
            if i % 2 == 0:
                res.extend(mapping[i][::-1])
            else:
                res.extend(mapping[i])
        return res


        
