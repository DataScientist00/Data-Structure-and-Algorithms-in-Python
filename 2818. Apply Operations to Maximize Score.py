#problem link-->> https://leetcode.com/problems/apply-operations-to-maximize-score/description/


from heapq import heappush, heappop
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        prime_scores = self.calculate_prime_scores(nums)
        left, right = self.calculate_subarray_contributions(prime_scores, n)
        
        # Max-heap to prioritize elements with higher values
        max_heap = []
        for i in range(n):
            heappush(max_heap, (-nums[i], i))
        
        result = 1
        while k > 0 and max_heap:
            value, i = heappop(max_heap)
            value = -value
            count = (i - left[i]) * (right[i] - i)
            operations = min(k, count)
            result = (result * pow(value, operations, MOD)) % MOD
            k -= operations
        
        return result

    def calculate_prime_scores(self, nums):
        max_num = max(nums)
        min_prime_factor = list(range(max_num + 1))
        for i in range(2, int(max_num**0.5) + 1):
            if min_prime_factor[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if min_prime_factor[j] == j:
                        min_prime_factor[j] = i
        
        prime_scores = []
        for num in nums:
            score = 0
            x = num
            while x > 1:
                prime = min_prime_factor[x]
                score += 1
                while x % prime == 0:
                    x //= prime
            prime_scores.append(score)
        
        return prime_scores

    def calculate_subarray_contributions(self, prime_scores, n):
        left = [-1] * n
        right = [n] * n
        stack = []
        
        # Calculate previous greater or equal elements
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack.clear()
        
        # Calculate next greater elements
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        return left, right
