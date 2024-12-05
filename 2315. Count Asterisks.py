#problem link--->> https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        for idx , i in enumerate(s.split('|')):
            for j in i:
                if idx % 2 == 0 and j == '*':
                    count += 1
        return count

        
