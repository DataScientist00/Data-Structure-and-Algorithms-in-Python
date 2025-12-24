# problem link-->> https://leetcode.com/problems/apple-redistribution-into-boxes/description/


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        h = []
        for i in range(len(capacity)):
            heapq.heappush(h , -1 * capacity[i])
        
        need = 0
        total = sum(apple)
        cnt = 0
        while h:
            need += 1
            temp = heapq.heappop(h)
            cnt += (-1 * temp)
            if cnt >= total:
                break
        return need
