#problem link--->>> https://leetcode.com/problems/merge-strings-alternately/description/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = []
        len1, len2 = len(word1), len(word2)
        
        
        for i in range(min(len1, len2)):
            temp.append(word1[i])
            temp.append(word2[i])
            
        
        if len1 > len2:
            temp.extend(word1[len2:])
        else:
            temp.extend(word2[len1:])
            
        return "".join(temp)

        
