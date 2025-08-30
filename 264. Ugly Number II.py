
# problem link->> https://leetcode.com/problems/ugly-number-ii/description/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visit = set()
        freq = [2,3,5]
        for i in range(n):
            num = heapq.heappop(heap)
            if i == n-1:
                return num
            for f in freq:
                if f * num not in visit:
                    visit.add(f*num)
                    heapq.heappush(heap , f*num)
             
        
