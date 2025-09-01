# problem link-->> https://leetcode.com/problems/maximum-average-pass-ratio/description/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(i,j):
            return (i+1)/(j+1) - i/j
        heap = []
        for n in classes:
            i , j = n
            ratio = gain(i , j)
            heapq.heappush(heap, (-ratio, (i, j)))  # heap ordered by ratio

        res = 0
        for n in range(extraStudents):
            r , tup = heapq.heappop(heap)
            i , j = tup
            i, j = i + 1, j + 1
            heapq.heappush(heap, (-gain(i, j), (i, j)))

            if n == extraStudents-1:
                while heap:
                    _, tup= heapq.heappop(heap)
                    i , j = tup
                    res += i / j
                break
        return res / len(classes)
                    


        
        
