#problem link-->> https://leetcode.com/problems/restore-ip-addresses/description/


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp , res = [] , []
        def backtrack(idx , i):
            if idx ==4 and i == len(s):
                res.append('.'.join(temp))
                return
            if idx > 4:
                return
            for j in range(i , min(i+3 , len(s))):
                if int(s[i:j+1]) <= 255 and (len(s[i:j+1]) == 1 or s[i] != '0'):
                    temp.append(s[i:j+1])
                    backtrack(idx+1 , j+1)
                    temp.pop()
        backtrack(0,0)
        return res

                
        
