from queue import Queue
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def minimumBinaryTreeHeight(self, root : TreeNode) -> int:
        if not root:
            return 0
        
        # quque to store the pending nodes
        pending_queue = Queue()
        # markdown all the visited nodes
        visited = dict()

