#problem link--->>> https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a , b = 0 , 0
        c , d = float('inf') , float('inf')
        for i in nums:
            if i > b:
                if i > a:
                    a , b = i , a
                else:
                     b = i
            if i < d:
                if i < c:
                    c , d = i , c
                else:
                    d = i
        return (a*b) - (c*d)
