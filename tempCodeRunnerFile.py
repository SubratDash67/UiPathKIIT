class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root: "TreeNode") -> str:
        def rserialize(node):
            if not node:
                return "n "
            return str(node.val) + " " + rserialize(node.left) + rserialize(node.right)

        return rserialize(root).strip()

    def deserialize(self, data: str) -> "TreeNode":
        def rdeserialize(vals):
            val = next(vals)
            if val == "n":
                return None
            node = TreeNode(int(val))
            node.left = rdeserialize(vals)
            node.right = rdeserialize(vals)
            return node

        val_iter = iter(data.split())
        return rdeserialize(val_iter)


solution = Solution()
tree = solution.deserialize("1 2 n n 3 4 n n 5 n n")
serialized_tree = solution.serialize(tree)
print(serialized_tree)
