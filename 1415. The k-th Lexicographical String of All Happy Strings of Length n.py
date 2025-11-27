# problem link-->> https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        temp = []
        check = ['a','b','c']
        cnt = 0
        ans = ''
        def backtrack():
            nonlocal cnt, ans
            if ans:       # early stop once found
                return
            if len(temp) == n:
                cnt += 1
                if cnt == k:
                    ans = ''.join(temp)
                    return
                return
            for ch in check:
                if temp and temp[-1] == ch:
                    continue
                temp.append(ch)
                backtrack()
                temp.pop()
                if ans:
                    return
        backtrack()
        return ans
        
