#problem link--> https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = [-int(num) for num in nums]
        heapq.heapify(maxheap)

        while k > 1:
            heapq.heappop(maxheap)
            k -= 1
        return str(-maxheap[0])
        
