# problem link-->> https://leetcode.com/problems/design-underground-system/description/


class UndergroundSystem:

    def __init__(self):
        self.checkinmap = {} # id -> (startstaion , time)
        self.totalmap = {} # (start , end) -> [totaltime , count]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinmap[id] = (stationName , t)

    def checkOut(self, id: int, endstation: str, t: int) -> None:
        start, time = self.checkinmap[id]
        route = (start , endstation)
        if route not in self.totalmap:
            self.totalmap[route] = [0,0]
        self.totalmap[route][0] += t - time
        self.totalmap[route][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total , count = self.totalmap[(startStation ,endStation )]
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
