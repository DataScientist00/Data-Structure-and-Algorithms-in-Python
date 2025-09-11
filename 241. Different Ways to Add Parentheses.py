# problem link-->> https://leetcode.com/problems/different-ways-to-add-parentheses/description/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operands = {
            '+' : lambda x , y: x + y,
            '-' : lambda x , y: x - y,
            '*' : lambda x , y: x * y
        }
        def solve(left , right):
            res = []
            for i in range(left , right+1):
                if expression[i] in operands:
                    nums1 = solve(left , i-1)
                    nums2 = solve(i+1 , right)
                    for n1 in nums1:
                        for n2 in nums2:
                            x = operands[expression[i]](n1 , n2)
                            res.append(x)

            if res == []:
                res.append(int(expression[left:right+1]))
            return res
        return solve(0 , len(expression)-1)


        
