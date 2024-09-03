#problem link-->> https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Node:
    def __init__(self):
        self.children = {}
        self.endswith = False

class Trie:

    def __init__(self):
        self.root = Node()
                
    def insert(self, word: str) -> None:
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.endswith = True
        
    def search(self, word: str) -> bool:
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return ptr.endswith
        
       
    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
