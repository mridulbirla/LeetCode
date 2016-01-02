# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q=[]
        self.print_bfs_values(root)
        self.idx=-1
        self.size=len(self.q)

    def print_bfs_values(self,node):
        if node is None:
            return
        self.print_bfs_values(node.left)
        self.q.append(node.val)
        self.print_bfs_values(node.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        self.idx += 1
        return self.idx < self.size
        
        
        

    def next(self):
        """
        :rtype: int
        """
        return self.q[self.idx]

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []