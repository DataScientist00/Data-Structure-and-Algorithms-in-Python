#problem link-->> https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse = True)
        pp = sum(nums)
        if pp % k != 0: return False
        total = pp/ k
        if nums[0] > total:
            return False
        visited = [False] * len(nums)
        def backtrack(i , k ,currsum):
            if k == 0:
                return True
            if total == currsum:
                return backtrack(0 , k-1 , 0)
            for j in range(i , len(nums)):
                #this condition ensures if if previous element is not visited and this one is same as before then why to go same path skip it 
                #(this will help prunning the unnecessary calls and avoid TLE)
                if j > 0 and not visited[j - 1] and nums[j] == nums[j - 1]:
                    continue
                if visited[j] == True or currsum + nums[j] > total:
                    continue
                visited[j] = True
                if backtrack(j , k , currsum+nums[j]):
                    return True
                visited[j] = False
            return False
        return backtrack(0,k,0)
