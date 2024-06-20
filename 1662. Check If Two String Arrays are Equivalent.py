#problem link--->> https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=w2=0
        a1=a2=0

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][a1] != word2[w2][a2]:
                return False
            a1,a2 = a1+1 , a2+1
            if a1 == len(word1[w1]):
                w1 += 1
                a1 =0
            if a2 == len(word2[w2]):
                w2 += 1
                a2 =0
        if w1 != len(word1) or w2 != len(word2):
                return False
        return True
            
        
