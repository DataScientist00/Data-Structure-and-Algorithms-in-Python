#problem link--->>> https://leetcode.com/problems/design-hashset/description/

class Helper:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash = [Helper(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        address = self.hash[key % len(self.hash)]
        while address.next != None:
            if address.next.key == key :
                return
            address = address.next
        address.next = Helper(key)
        

    def remove(self, key: int) -> None:
        address = self.hash[key % len(self.hash)]
        while address.next != None:
            if address.next.key == key :
                address.next = address.next.next
                return
            address = address.next
        
        

    def contains(self, key: int) -> bool:
        address = self.hash[key % len(self.hash)]
        while address.next != None:
            if address.next.key == key :
                return True
            address = address.next
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
