# problem link-->> https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/


class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(i,cur_sum,target):
            num =  str(target * target) # Geting the i*i
            if i == len(num) and cur_sum == target:
                return True
            for j in range(i , len(num)):
                temp_sum = int(num[i:j+1])
                if partition(j+1 , cur_sum + temp_sum , target):
                    return True
            return False


        ans = 0
        for i in range(1,n+1):
            if partition(0,0,i):
                ans += i * i
        return ans
        
