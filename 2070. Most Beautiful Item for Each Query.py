
# problem link-->> https://leetcode.com/problems/most-beautiful-item-for-each-query/description/

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0] , -x[1]))

        ans = []

        max_beauty = 0
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty

        for q in queries:
            l = 0
            r = len(items)-1
            candidate = -1
            while l <= r:
                mid = (l+r)//2
                if items[mid][0] <= q:
                    l = mid + 1
                    candidate = mid
                else:
                    r= mid - 1
            ans.append(items[candidate][1] if candidate != -1 else 0)
        return ans

        
