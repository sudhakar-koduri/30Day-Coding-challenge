from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigzag_level_order(root):

    result = []
    l_r = True
    child_nodes = None
    level_nodes = None
    node = root
    lvl_res = []

    while node:
        if not child_nodes:
           child_nodes = deque()
        lvl_res.append(node.data)
        if l_r:
          if node.left:
             child_nodes.append(node.left)
          if node.right:
             child_nodes.append(node.right)
        else:
          if node.right:
             child_nodes.append(node.right)       
          if node.left:
             child_nodes.append(node.left)
        
        node = None
        if level_nodes == None or len(level_nodes) == 0:
            result.append(lvl_res.copy())
            lvl_res.clear()
            level_nodes = child_nodes
            child_nodes = None
            l_r = not l_r
        if level_nodes != None and len(level_nodes) > 0:
           node = level_nodes.pop()
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(10)
print(zigzag_level_order(root))


def zigzag_level_order_sol(root):
    if root is None:
        return []

    results = []
    dq = deque([root])
    reverse = False

    while len(dq):
        size = len(dq)
        results.insert(len(results), [])

        for i in range(size):
            if not reverse:
                node = dq.popleft()
                results[len(results) - 1].append(node.data)
            
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                node = dq.pop()
                results[len(results) - 1].append(node.data)

                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left) 

        reverse = not reverse

    return results