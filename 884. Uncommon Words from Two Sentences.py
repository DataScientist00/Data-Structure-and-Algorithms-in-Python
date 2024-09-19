#problem link-->> https://leetcode.com/problems/uncommon-words-from-two-sentences/description/


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        res = []
        for a in s2.split():
            c1[a] += 1
        for a in c1:
            if c1[a] == 1 :
                res.append(a)
        return res
        
