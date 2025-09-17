# problem link-->> https://leetcode.com/problems/sentence-similarity-iii/description/

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) > len(s2):
            s1,s2=s2,s1
        
        i = 0
        j = len(s1)-1
        k = 0
        l = len(s2)-1
        for _ in range(len(s1)):
            if s1[i] == s2[k]:
                i += 1
                k += 1
            elif s1[j] == s2[l]:
                j -= 1
                l -= 1
        return i > j 


        
        
