#problem link-->> https://leetcode.com/problems/maximum-number-of-removable-characters/description/

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def issubseq(s , subseq):
            i1 , i2 = 0 , 0
            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subseq)

        res = 0
        l , r = 0 , len(removable) -1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m+1])
            if issubseq(s , p):
                res = max(res , m+1)
                l = m+1
            else:
                r = m-1
        return res
        
