# problem link-->> https://leetcode.com/problems/minimize-xor/description/



class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(num):
            res = 0
            while num > 0:
                res += num & 1
                num = num >> 1
            return res

        cnt1 , cnt2 = count_bits(num1) , count_bits(num2)
        i = 0
        x = num1

        # Remove least significant bit
        while cnt1 > cnt2:
            if x & (1 << i):
                cnt1 -= 1
                x = x ^ (1 << i)
            i += 1
        # Add least significant bit
        while cnt1 < cnt2:
            if x & (1 << i) == 0:
                cnt1 += 1
                x = x | (1 << i)
            i += 1

        return x


        
