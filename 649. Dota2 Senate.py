# problem link-->> https://leetcode.com/problems/dota2-senate/description/


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque() # Queue for Radiant senators
        dire = deque() # Queue for Dire senators

        for i, v in enumerate(senate):
            if v == "R":  # If the senator belongs to Radiant, store the index in the Radiant queue
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r_index = radiant.popleft() # Get the next Radiant senator
            d_index = dire.popleft()

            if r_index < d_index: # Radiant senator acts first and bans the Dire senator
                radiant.append(r_index + len(senate))
            else:
                dire.append(d_index + len(senate))
        
        return "Radiant" if radiant else "Dire" # # The party with remaining senators wins
