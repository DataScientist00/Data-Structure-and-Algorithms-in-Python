# problem link-->> https://leetcode.com/problems/count-vowel-strings-in-ranges/description/


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)
        vowels = set('aeiou')
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        res = []
        for l,r in queries:
            ans = prefix[r] - (prefix[l-1] if l-1 >= 0 else 0)
            res.append(ans)
        return res
