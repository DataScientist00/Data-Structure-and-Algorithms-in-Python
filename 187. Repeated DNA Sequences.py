#problem link-->> https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        see, res = set() , set()
        for l in range(len(s) - 9):
            cur = s[l : l+ 10]
            if cur in see:
                res.add(cur)
            see.add(cur)
        return list(res)
        
