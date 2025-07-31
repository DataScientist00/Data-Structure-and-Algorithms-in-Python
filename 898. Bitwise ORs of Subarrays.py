# problem link-->> https://leetcode.com/problems/bitwise-ors-of-subarrays/description/

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev = set()
        curr = set()
        for i in range(len(arr)):
            curr = {arr[i]}
            for n in prev:
                curr.add(n | arr[i])
            ans |= curr
            prev = curr
        return len(ans)

        
