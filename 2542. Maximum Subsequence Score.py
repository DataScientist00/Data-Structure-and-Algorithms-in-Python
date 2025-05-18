# problem link-->> https://leetcode.com/problems/maximum-subsequence-score/description/

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1 , n2) for n1 , n2 in zip(nums1,nums2)]
        pairs = sorted(pairs , key = lambda p:p[1] , reverse = True)

        minheap = []
        n1sum = 0
        res = 0
        for n1 , n2 in pairs:
            n1sum += n1
            heapq.heappush(minheap , n1)

            if len(minheap) > k:
                n1pop = heapq.heappop(minheap)
                n1sum -= n1pop

            if len(minheap) == k:
                res = max(res , n1sum * n2)
        return res
        
