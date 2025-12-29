# problem link-->> https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        start_time =[fl[0] for fl in flowers]
        start_time.sort()
        end_time = [fl[1] for fl in flowers]
        end_time.sort()

        def up(p):
            l , r =0 , len(flowers)-1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if start_time[m] <= p:
                    l = m +1
                    ans = l
                else:
                    r = m -1
            return 0 if ans == -1 else ans
        
        def lp(p):
            l,r = 0, len(flowers)-1
            ans=-1
            while l<=r:
                m=l+(r-l)//2

                if end_time[m]>=p:
                    r=m-1
                else:
                    l=m+1
                    ans=l
            return 0 if ans==-1 else ans

        ans = []
        for p in people:
            upper_bound = up(p)
            lower_bound = lp(p)
            ans.append(upper_bound - lower_bound)
        return ans
        


        
