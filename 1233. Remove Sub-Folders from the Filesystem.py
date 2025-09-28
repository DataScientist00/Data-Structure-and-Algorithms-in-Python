# problem link-->> https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/




# Trie Solution -------------------------------------------------

class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add(self , path):
        node = self
        for f in path.split('/'):
            if f not in node.children:
                node.children[f] = Trie()
            node = node.children[f]
        node.is_end = True

    def check_prefix(self , path):
        node = self
        folder = path.split('/')
        for f in range(len(folder)-1):
            node = node.children[folder[f]]
            if node.is_end:
                return True
        return False
            

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.check_prefix(f):
                res.append(f)
        return res



# Simple Solution Big_oh(N * L ^ 2)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = set(folder)
        res = []
        for f in folder:
            res.append(f)
            for t in range(len(f)):
                if f[t] == '/' and f[:t] in folders:
                    res.pop()
                    break
        return res
        




        
