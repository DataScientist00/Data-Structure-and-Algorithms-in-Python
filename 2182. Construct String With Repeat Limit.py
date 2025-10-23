# problem link-->> https://leetcode.com/problems/construct-string-with-repeat-limit/description/


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        heap = [(-ord(i) , cnt) for i , cnt in count.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            char , cnt  = heapq.heappop(heap)
            char = chr(-char)
            cur_cnt = min(cnt , repeatLimit)
            res.append(cur_cnt * char)

            if cnt - cur_cnt > 0 and heap:
                next_char , next_cnt  = heapq.heappop(heap)
                next_char = chr(-next_char)
                res.append(next_char)
                if next_cnt > 1:
                    heapq.heappush(heap , (-ord(next_char) , next_cnt-1))
                heapq.heappush(heap , (-ord(char) , cnt - cur_cnt))
        return "".join(res)



        
