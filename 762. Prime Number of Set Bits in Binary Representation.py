# problem link -- >> https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2 , int(n ** 0.5)+1):
                if n % i == 0:
                    return False
            return True


        ans = 0
        for n in range(left , right+1):
            set_bits = 0
            temp = bin(n).count('1')
            if is_prime(temp):
                ans += 1
        return ans






        
