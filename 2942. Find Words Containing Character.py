#problem link-->> https://leetcode.com/problems/find-words-containing-character/description/


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        cnt = 0
        for word in words:
            for c in word:
                if c == x[0] and cnt not in ans:
                    ans.append(cnt)
            cnt += 1
        return ans
        
