#problem link-->> https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = 'aeiou'

        def substringsWithAtMost(k: int) -> int:
            if k < 0:
                return 0
            res = 0
            vowels_count = 0
            unique_vowels = 0
            vowel_last_seen = {}
            l = 0
            for r, c in enumerate(word):
                if c in vowels:
                    vowels_count += 1
                    if c not in vowel_last_seen or vowel_last_seen[c] < l:
                        unique_vowels += 1
                    vowel_last_seen[c] = r
                while r - l + 1 - vowels_count > k:
                    if word[l] in vowels:
                        vowels_count -= 1
                        if vowel_last_seen[word[l]] == l:
                            unique_vowels -= 1
                    l += 1
                if unique_vowels == 5:
                    res += min(vowel_last_seen[vowel] for vowel in vowels) - l + 1
            return res

        return substringsWithAtMost(k) - substringsWithAtMost(k - 1)
