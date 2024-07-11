#problem link-->>  https://leetcode.com/problems/first-unique-character-in-a-string/description/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for a in s:
            count[a] = count[a] + 1
        for i , a in enumerate(s):
            if count[a] == 1:
                return i 
        return -1
        
