# problem link-->> https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for k , v in a.items():
            if k not in b or b[k] < v:
                return False
        return True
        
