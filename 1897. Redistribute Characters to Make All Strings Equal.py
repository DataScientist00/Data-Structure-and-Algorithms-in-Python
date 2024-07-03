#problem link-->> https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        temp = defaultdict(int)

        for word in words:
            for char in word:
                temp[char] += 1
        for i in temp:
            if temp[i] % len(words):
                return False
        return True
        
