# problem link-->> https://leetcode.com/problems/shifting-letters-ii/description/


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s)+1)
        for l , r , k in shifts:
            prefix[r+1] += 1 if k else -1
            prefix[l] += -1 if k else 1

        temp = [ord(c) - ord('a') for c in s]
        
        diff = 0
        for i in reversed(range(len(prefix))):
            diff += prefix[i]
            temp[i-1] = (diff + temp[i-1]) % 26

        res = [chr(ord('a')+ c) for c in temp]
        return ''.join(res)

        
