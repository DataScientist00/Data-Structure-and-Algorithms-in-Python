#problem link -->> https://leetcode.com/problems/longest-palindrome/description/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag = 0
        count = Counter(s)
        res = 0
        if len(s) == 1:
            return 1
        for i in count.values():
            if int(i) % 2 == 0:
                res = res + i
            else:
                flag +=1
                res = res + (i-1)
        return res+1 if flag != 0 else res


        
        
        
