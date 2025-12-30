# problem link -->> https://leetcode.com/problems/most-profit-assigning-work/description/


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        paired = list(zip(difficulty , profit))
        paired.sort(key = lambda x: x[0])
        difficulty , profit = zip(*paired)
        difficulty = list(difficulty)
        profit = list(profit)

        def getdiff(w):
            low , high = 0 , len(difficulty)-1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if difficulty[mid] <= w:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if idx == -1:
                return 0
            return max(profit[:idx + 1])

        total = 0
        for w in worker:
            total += getdiff(w)
        return total
        
