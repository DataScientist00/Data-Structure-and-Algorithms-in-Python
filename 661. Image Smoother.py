#problem link--->>> https://leetcode.com/problems/image-smoother/description/


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        temp = [[0] *cols for _ in range(rows) ]

        for i in range(rows):
            for j in range(cols):
                res , count = 0 , 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if k < 0 or k == rows or l < 0 or l == cols:
                            continue
                        res += img[k][l]
                        count += 1
                temp[i][j] = res // count
        return temp
        
