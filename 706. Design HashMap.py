#Problem Link ----> https://leetcode.com/problems/design-hashmap/description/


class Listnode:
    def __init__(self,key=-1,value=-1,next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.Hashmap = [Listnode() for i in range(1000)]

    def Hashfunction(self,key):
        return key % len(self.Hashmap)

        
    def put(self, key: int, value: int) -> None:
        cur = self.Hashmap[self.Hashfunction(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = Listnode(key,value)
        

    def get(self, key: int) -> int:
        cur = self.Hashmap[self.Hashfunction(key)]
        while cur:
            if cur.key == key:
                return cur.value
            cur=cur.next
        return -1
        

    def remove(self, key: int) -> None:
        cur = self.Hashmap[self.Hashfunction(key)]
        while cur and cur.next:
            if cur.next.key ==key:
                cur.next=cur.next.next
            cur=cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
