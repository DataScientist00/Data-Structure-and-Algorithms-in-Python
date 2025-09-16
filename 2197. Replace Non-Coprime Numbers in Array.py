# problem link -->> https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/


import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            stack.append(nums[i])
            while len(stack) > 1 and math.gcd(stack[-1] , stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(math.lcm(a,b))
        return stack
