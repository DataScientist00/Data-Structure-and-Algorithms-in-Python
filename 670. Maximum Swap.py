# problem link-->> https://leetcode.com/problems/maximum-swap/description/


class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = []
        for i,n in enumerate(str(num)):
            temp.append(int(n))
        tt = {n: i for i, n in enumerate(temp)}
        for i,n in enumerate(temp):
            for j in range(9,n,-1):
                if j in tt and tt[j] > i:
                    temp[i] , temp[tt[j]] = temp[tt[j]] , temp[i]
                    number = int("".join(map(str, temp)))
                    return number

        return num



        
