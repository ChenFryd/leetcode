# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        output = [root] if root else []
        while queue:
            root = queue.pop(0)
            output.append(root)
            if not root:
                continue
            queue.append(root.left)
            queue.append(root.right)
        return output

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return []
        print(data)
        output = [TreeNode(data[0])] 
        for i in range(data):
            output[i].left = TreeNode(data[2*i])
            output[i].right = TreeNode(data[2*i+1])
        return output

            
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = [1,2,3,None,None,4,5]
ans = deser.deserialize(ser.serialize(root))

# Runtime: 92 ms, faster than 98.78% of Python3 online submissions for Serialize and Deserialize Binary Tree.
print(ser.serialize(deser.deserialize([1,2,3,None,None,4,5])))