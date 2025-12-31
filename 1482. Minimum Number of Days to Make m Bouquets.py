# problem link-->> https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


class Solution:
    def countDays(self,arr,n,k):
        s = 0
        count = 0 
        for i in arr : 
            if  i <= n : 
                count += 1 
                if count == k: 
                    s += 1 
                    count = 0
            else : 
                count = 0 
        return s
            
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        low = min(arr)
        high = max(arr)
        temp = -1
        while low <= high : 
            mid = (low+high)//2

            val = self.countDays(arr,mid,k)
            
            if val >= m : 
                temp = mid
                high = mid - 1 
            else : 
                low = mid + 1 
        
        return temp
        
