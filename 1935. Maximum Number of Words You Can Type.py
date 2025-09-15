# problem link-->> https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/


class Solution:
    def canBeTypedWords(self, text: str, c: str) -> int:
        text = text.split(' ')
        ans = 0
        check = set(c)
        for t in text:
            for i in t:
                if i  in check:
                    ans += 1
                    break                  
        return len(text)-ans
