# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        n = len(preorder)
        for i in range(1, n):
            pt1 = root
            inserted = False
            while not inserted:
                if preorder[i] < pt1.val:
                    if pt1.left is None:
                        pt1.left = TreeNode(preorder[i])
                        inserted = True
                    else:
                        pt1 = pt1.left
                else:
                    if pt1.right is None:
                        pt1.right = TreeNode(preorder[i])
                        inserted = True
                    else:
                        pt1 = pt1.right
        return root
# * Runtime ~ 34ms
# * Faster than 70% Solution in First try