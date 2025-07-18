# problem link-->>>> https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice , bob = 0,0
        for i in range(1 , len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    alice += 1
                if colors[i] == "B":
                    bob += 1
        return alice > bob
        
