# problem link-->> https://leetcode.com/problems/avoid-flood-in-the-city/description/



class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        heap = []  # stores indices of days we can dry lakes
        lake = {}  # stores last day a lake was filled
        ans = [-1] * len(rains)

        for i, r in enumerate(rains):
            if r == 0:
                heapq.heappush(heap, i)
                ans[i] = 1 
            else:
                if r in lake:
                    if not heap:
                        return []
                    # Find the earliest zero day after last rain
                    found = False
                    temp = []
                    while heap:
                        dry_day = heapq.heappop(heap)
                        if dry_day > lake[r]:
                            ans[dry_day] = r
                            found = True
                            break
                        else:
                            temp.append(dry_day)
                    # push back unused zero days
                    for d in temp:
                        heapq.heappush(heap, d)
                    if not found:
                        return []
                lake[r] = i

        return ans
