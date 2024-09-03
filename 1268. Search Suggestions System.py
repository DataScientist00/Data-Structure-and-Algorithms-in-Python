#problem link-->> https://leetcode.com/problems/search-suggestions-system/description/


class Node:
    def __init__(self):
        self.children = {}
        self.index = []

class Solution:
    def __init__(self):
        self.root = Node()
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # Sort products lexicographically

        def build_trie():
            for idx, word in enumerate(products):
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = Node()
                    node = node.children[char]
                    node.index.append(idx)
                    if len(node.index) > 3:
                        node.index = node.index[:3]  # Only keep top 3 suggestions
        
        def search():
            node = self.root
            result = []
            for char in searchWord:
                if node is not None and char in node.children:
                    node = node.children[char]
                    result.append(node.index)
                else:
                    result.append([])  # No match found
                    node = None  # Stop further searching
            return result
        
        build_trie()
        index_lists = search()

        # More readable version of the return statement
        final_result = []
        for indices in index_lists:
            suggestion = []
            for i in indices:
                suggestion.append(products[i])
            final_result.append(suggestion)

        return final_result







        
