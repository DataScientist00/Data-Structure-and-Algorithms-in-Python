# problem link-->> https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        heap = []   # (leave_time, chair_number)
        times = [(t[0], t[1], i) for i, t in enumerate(times)]  # keep friend index
        times.sort()
        
        next_chair = 0
        free = []   # min-heap of available chairs

        for t1 , t2, friend in times:
            while heap and heap[0][0] <= t1:
                leave_time , chair = heapq.heappop(heap)
                heapq.heappush(free , chair)

            if free:
                chair  = heapq.heappop(free)
            else:
                chair = next_chair
                next_chair += 1
            if targetFriend == friend:
                return chair
            heapq.heappush(heap , (t2 , chair))
