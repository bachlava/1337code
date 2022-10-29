"""
Given the root of an n-ary tree, return the preorder traversal of its 
nodes' values.
Nary-Tree input serialization is represented in their level order 
traversal. 
Each group of children is separated by the None value (See examples)
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        result = [root.val]
        if not root.children:
            return result
        for child in root.children:
            result.extend(self.preorder(child))
        return result


if __name__ == '__main__':
    root1 = Node(1, [
        Node(3, [
            Node(5),
            Node(6)
            ]),
        Node(2),
        Node(4)
        ])
    print(Solution().preorder(root1))

    root2 = Node(1, [
        Node(2),
        Node(3, [
            Node(6, []),
            Node(7, [
                Node(11, [
                    Node(14)
                ])
                ])
            ]),
        Node(4, [
            Node(8, [
                Node(12)
            ]),
        ]),
        Node(5, [
            Node(9, [
                Node(13)
            ]),
            Node(10)
        ])
        ])
    print(Solution().preorder(root2))
