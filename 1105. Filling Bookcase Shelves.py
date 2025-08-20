# problem link-->> https://leetcode.com/problems/filling-bookcase-shelves/description/


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = {}
        def solve(i , maxHeight , width):
            if i == len(books):
                return maxHeight
            if (i , maxHeight , width) in memo:
                return memo[i , maxHeight , width] 
            thickness , height = books[i]
            keep , skip = float('inf'),float('inf')
            if width >= thickness:
                keep = solve(i+1 , max(maxHeight ,height) , width - thickness)
            skip = maxHeight + solve(i+1 , height , shelfWidth - thickness)
            memo[i , maxHeight , width]  = min(keep , skip)
            return memo[i , maxHeight , width]

        return solve(0,0 , shelfWidth)
        
