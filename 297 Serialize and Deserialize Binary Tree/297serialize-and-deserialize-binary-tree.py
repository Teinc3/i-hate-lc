# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        output = ""
        if not root:
            return output

        layers = [root]
        while layers:
            new_layers = []
            for node in layers:
                if not node:
                    output += "None" + ","
                    continue
                output += str(node.val) + ","
                new_layers.append(node.left)
                new_layers.append(node.right)
            layers = new_layers
        
        return output.rstrip(",")
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None

        data = [TreeNode(int(val)) if val != "None" else None for val in data.split(',')]
        if not data:
            return None
        
        counter = 1
        level_nodes = [data[0]]
        new_nodes = []
        while counter < len(data):
            for node in level_nodes:
                node.left = data[counter]
                node.right = data[counter + 1]
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                counter += 2
            
            level_nodes = new_nodes
        
        return data[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))