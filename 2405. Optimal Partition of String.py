#problem link-->> https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution:
    def partitionString(self, s: str) -> int:
        count = set()
        res = 1
        for i in s:
            if i in count:
                res += 1
                count = set()
            count.add(i)
        return res
        
            
        
