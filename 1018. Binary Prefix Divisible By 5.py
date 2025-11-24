# problem lin-->> https://leetcode.com/problems/binary-prefix-divisible-by-5/description/


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        binary = 0
        for n in nums:
            binary = (binary << 1 | n)
            if int(binary) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
        
