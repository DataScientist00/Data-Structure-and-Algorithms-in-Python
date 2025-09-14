#problem link--> https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.hash_set = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        st = startTime
        et = endTime
        if len(self.hash_set) == 0:
            self.hash_set.append([st,et])
            return True
        for l,r in self.hash_set:
            if not (et <= l or st >= r):
                return False        
        self.hash_set.append([st,et])
        return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
