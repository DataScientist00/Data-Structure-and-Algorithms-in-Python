# problem link-->> https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        flag = True
        i = 1
        if n % 2 == 0:
            for k in range((n)):
                if k < n // 2:
                    res.append(i)
                    i += 1
                else:
                    i -= 1
                    res.append(-i)
            return res
        else:
            for k in range((n)):
                if k < n // 2:
                    res.append(i)
                    i += 1
                else:
                    if flag:
                        res.append(0)
                        flag = False
                        continue
                    i -= 1
                    res.append(-i)
            return res
            
        
