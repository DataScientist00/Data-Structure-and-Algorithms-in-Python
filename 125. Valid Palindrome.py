# problem link-->> https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        temp = ''
        for i in s:
            if not i.isalnum():
                continue
            temp += i
        return temp == temp[::-1]

        
