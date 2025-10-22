# problem link-->> https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/


# ---------Solution-1. Range Interval pattern-------------

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        store = []
        for n in nums:
            store.append((n-k , n+k))

        store.sort()
        q = deque()
        res = 0
        for a,b in store:
            while q and q[0][1] < a:
                q.popleft()
            q.append((a,b))
            res = max(res , len(q))
        return res

  # --------Solution 2. Binary Search-----------------------

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        def binarysearch(x):
            l = 0
            r = len(nums)-1
            ans = 0
            while l <= r:
                mid = (l+r)//2
                if x >= nums[mid]:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid -1
            return ans


        nums.sort()
        res = 0
        for i,n in enumerate(nums):
            y = n+2*k # Equatioin 
            temp = binarysearch(y)
            print(temp)
            res = max(res , temp-i+1)
        return res

        
