
# problem link-->> https://leetcode.com/problems/prime-subtraction-operation/description/

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            for f in range(2 , int(sqrt(n))+1):
                if n % f == 0:
                    return False
            return True

        prev_p = 0
        for n in nums:
            upperbound = n - prev_p
            largest_prime = 0
            for r in reversed(range(2 ,upperbound)):
                if is_prime(r):
                    largest_prime = r
                    break
            if n - largest_prime <= prev_p:
                return False
            prev_p = n - largest_prime
        return True
        
