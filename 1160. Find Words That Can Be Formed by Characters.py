#problem link-->>> https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars) #creating hash of chars
        res =0
        for w in words:
            cur_word = defaultdict(int) #this returns 0 if char not present
            flag = True
            for c in w:
                cur_word[c] += 1
                if c not in count or cur_word[c] > count[c]:
                    flag = False
                    break
            if flag:
                res += len(w)
        return res
        
