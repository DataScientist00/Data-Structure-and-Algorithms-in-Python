# problem link -- >> https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        plus = 0
        product = 1
        temp = n
        while temp>0:
            digit=temp%10
            plus =plus+digit
            product=product*digit
            temp=int(temp/10)
        return (product-plus)
        
