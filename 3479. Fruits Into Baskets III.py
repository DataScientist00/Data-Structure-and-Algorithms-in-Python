# problem link-->> https://leetcode.com/problems/fruits-into-baskets-iii/description/

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        seg = [0] * (4 * n)

        def build(node, left, right):
            if left == right:
                seg[node] = baskets[left]
                return
            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            seg[node] = max(seg[node * 2], seg[node * 2 + 1])

        def find_and_use(node, left, right, fruit):
            if seg[node] < fruit:
                return -1
            if left == right:
                seg[node] = -1
                return left
            mid = (left + right) // 2
            if seg[node * 2] >= fruit:
                res = find_and_use(node * 2, left, mid, fruit)
            else:
                res = find_and_use(node * 2 + 1, mid + 1, right, fruit)
            seg[node] = max(seg[node * 2], seg[node * 2 + 1])
            return res

        build(1, 0, n - 1)

        unplaced = 0
        for fruit in fruits:
            if find_and_use(1, 0, n - 1, fruit) == -1:
                unplaced += 1

        return unplaced
