# problem link-->> https://leetcode.com/problems/xor-queries-of-a-subarray/description/


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] ^ n)
        res = []
        for n1 , n2 in queries:
            res.append(prefix[n2+1] ^ prefix[n1])
        return res
