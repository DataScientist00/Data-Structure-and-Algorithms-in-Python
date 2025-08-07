# problem link-->> https://leetcode.com/problems/average-waiting-time/description/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        var = customers[0][0]
        summ = 0
        waiting_time = 0
        t = 0
        for n in customers:
            t1 , t2 = n
            t = max(var ,t1) + t2
            waiting_time = t - t1
            summ += waiting_time
            var = t
        return summ / len(customers)

        
