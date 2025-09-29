# problem link-->> https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.copy = set()
        self.ans = float('-inf')
        def bruteforce(i):
            if i >= len(s):
                self.ans = max(self.ans, len(self.copy))
                return
            for j in range(i+1 , len(s)+1):
                if s[i:j] in self.copy:
                    continue
                self.copy.add(s[i:j])
                bruteforce(j)
                self.copy.remove(s[i:j])        

        bruteforce(0)
        return self.ans
        
