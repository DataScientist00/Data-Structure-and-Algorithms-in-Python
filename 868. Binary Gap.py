# problem link -- >> https://leetcode.com/problems/binary-gap/description/


class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        prev = 0
        ans = float('-inf')
        for i in range(len(n)):
            if n[i] == '1':
                curr = i
                if curr != prev:
                    ans = max(ans , curr - prev)
                prev = curr
        return ans if ans != float('-inf') else 0
                



        
