# problem link-->> https://leetcode.com/problems/four-divisors/description/


class Solution:
    def checkDivisors(self, num: int) -> int:
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if num // i == i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(num // i)

        if len(divisors) == 4:
            return sum(divisors)
        else:
            return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result += self.checkDivisors(nums[i])

        return result
        
