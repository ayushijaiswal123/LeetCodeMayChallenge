# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = {}
        queue = [(root,0,0)]
        while len(queue) > 0:
            current_node, parent_node, depth = queue.pop()
            nodes[current_node.val] = [parent_node, depth]
            
            if current_node.left:
                queue.append((current_node.left, current_node.val, depth+1))
            if current_node.right:
                queue.append((current_node.right, current_node.val, depth+1))
            print(nodes)
        return nodes[x][1] == nodes[y][1] and (nodes[x][0] != nodes[y][0])
