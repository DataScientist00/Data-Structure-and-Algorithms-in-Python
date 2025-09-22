# problem link-->> https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/



class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap , -n)
        res = 0
        while k:
            n = heapq.heappop(heap)
            n = -n
            res += n
            heapq.heappush(heap , -1 * ceil(n / 3))
            k -= 1
        return res        
