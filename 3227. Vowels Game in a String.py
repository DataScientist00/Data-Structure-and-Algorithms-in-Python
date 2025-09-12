# problem link-->> https://leetcode.com/problems/vowels-game-in-a-string/description/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 0
        check = set('aeiou')
        for i in s:
            if i in check:
                vowels += 1
        return False if vowels == 0 else True
        
