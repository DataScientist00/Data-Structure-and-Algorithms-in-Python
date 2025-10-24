# problem link-->> https://leetcode.com/problems/next-greater-numerically-balanced-number/description/


# -----------Backtrack Solution-----------------

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        size = len(str(n))
        total = [0,1,2,3,4,5,6,7,8,9]
        def backtrack(num , numleft):
            if numleft == 0:
                for d in range(1,9):
                    if total[d] != 0 and total[d] != d:
                        return -1
                return num if num > n else -1
            result = -1
            for d in range(1,9):
                if total[d] > 0 and total[d] <= numleft:
                    total[d] -= 1
                    result = backtrack(num * 10 + d , numleft-1)
                    total[d] += 1
                if result != -1:
                    break
            return result

        res = backtrack(0,size)
        if res == -1:
            res = backtrack(0,size+1)
        return res
        
