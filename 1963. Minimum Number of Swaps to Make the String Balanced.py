#problem link-->> https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/


class Solution:
    def minSwaps(self, s: str) -> int:
        count , matches = 0 , 0
        for i in s:
            if i == '[':
                count -=1
            else:
                count +=1
            matches = max(count , matches)
        return (matches +1) // 2
        
