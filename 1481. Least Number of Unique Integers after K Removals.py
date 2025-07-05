# problem link--> https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # BUCKET SORT SOLUTION
        freq = Counter(arr)
        freq_list = [0] * (len(arr) + 1)

        for n , f in freq.items():
            freq_list[f] += 1

        res = len(freq)
        for f in range(1 , len(freq_list)):
            remove = freq_list[f]
            if k >= f* remove:
                k -= f * remove
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        return res
