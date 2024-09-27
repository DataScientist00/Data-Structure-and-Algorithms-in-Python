#problem link-->> https://leetcode.com/problems/lemonade-change/description/


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        print(bills)
        ans = {5:0 , 10:0}
        flag = True
        for b in bills:
            if b == 5:
                ans[b] += 1
            elif b == 10:
                if ans[5] > 0:
                    ans[10] += 1
                    ans[5] -= 1
                else:
                    flag = False
                    break
            else:
                if ans[10] > 0 and ans[5] > 0:
                    ans[10] -= 1
                    ans[5] -= 1
                elif ans[5] >= 3:
                    ans[5] -= 3
                else:
                    flag = False
                    break
        return flag
            

        
