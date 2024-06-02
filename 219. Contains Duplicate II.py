# Problem link -->>> https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k :
                temp.remove(nums[left])
                left += 1
            if nums[right] in temp:
                return True
            temp.add(nums[right])
        return False

        


            
        
