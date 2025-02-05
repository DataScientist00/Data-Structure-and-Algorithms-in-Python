#problem link-->> https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        for i in range(len(s)-k+1):
            hashset.add(s[i:i+k])
        return len(hashset) == 2 ** k
        
