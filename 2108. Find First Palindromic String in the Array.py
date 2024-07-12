#problem link-->> https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            left = 0
            right = len(w) - 1
            while w[left] == w[right]:
                if left >= right:
                    return w
                left +=1
                right -=1
        return ""
        
