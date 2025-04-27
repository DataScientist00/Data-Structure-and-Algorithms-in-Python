# problem link-->> https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        ans = 0
        total =0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                l += 1

            ans = max(ans , total)
        return ans
                


        
