# problem link -- >> https://leetcode.com/problems/truncate-sentence/description/?cong=true


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()
        s = ''
        cnt = 0
        for i in a[:k]:
            s = s + i
            cnt += 1
            if cnt < k:
                s = s + ' '
        return s
        
        
