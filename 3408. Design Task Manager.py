
# problem link-->> https://leetcode.com/problems/design-task-manager/description/


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []

        for u,t,p in tasks:
            heapq.heappush(self.heap , (-p,-t,u,t))
            self.task_map[t] = (u,p)

    def add(self, u: int, t: int, p: int) -> None:
        heapq.heappush(self.heap , (-p,-t,u,t))
        self.task_map[t] = (u,p)

    def edit(self, t: int, newPriority: int) -> None:
        u,p = self.task_map[t]
        self.task_map[t] = ((u,newPriority))
        heapq.heappush(self.heap , (-newPriority,-t,u,t))

    def rmv(self, t: int) -> None:
        if t in self.task_map:
            del self.task_map[t]

    def execTop(self) -> int:
        while self.heap:
            p,t,u,task_id = heapq.heappop(self.heap)
            p = -p
            t = -t
            if t in self.task_map:
                user_id , new_priority = self.task_map[t]
                if new_priority == p:
                    del self.task_map[t]
                    return user_id
        return -1
            
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
