# problem link-->> https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y = 0
        for i in range(n):
            y += (1 if customers[i] == 'Y' else 0)
        
        min_p = n
        hour = n
        y_found = 0
        n_found = 0
        for h in range(n+1):
            y_remaining = y - y_found
            pen = y_remaining + n_found
            if pen < min_p:
                hour = h
                min_p = pen
            n_found += (1 if h < n and customers[h] == 'N' else 0)
            y_found += (1 if h < n and customers[h] == 'Y' else 0)
        return hour
       
