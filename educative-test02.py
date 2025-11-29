from collections import deque 
# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# from ds_v1.BinaryTree.BinaryTree import TreeNode

# We try to cover from leaf nodes since in tree, lower level got more/same number of nodes than its parent level.
# input that takes the root node to postorder traverse and the camera count found so far 
# return the state, camera count ;
# State values: 0 - uncovered; 1- covered; 2- Camera installed
def dfs(root, cam):
    if (root == None):
        return (1, cam)
    lt, cam = dfs(root.left, cam)
    rt, cam = dfs(root.right, cam)
    # Install camera if either child is uncovered
    if (lt == 0 or rt == 0):
        cam += 1
        return (2, cam)
    # If either of the child got camera, the current one is covered.
    if (lt == 2 or rt == 2):
        return (1, cam)
    # The current node is uncovered
    return (0, cam)

def minCameraCover(root):
    ans, cam = dfs(root, 0)
    if ans == 0:
        return cam+1
    else :
        return cam

#  Test code to generate the input tree
def buildTree(input):
    next = 0
    max_len = len(input)
    root = TreeNode(input[next])
    next += 1
    que = deque([root])
    isleft = True 
    while next < max_len:
        if isleft:
            curr = que.popleft()
        if input[next] != None:
            node = TreeNode(input[next])
            if isleft:
                curr.left = node 
            else:
                curr.right = node
            que.append(node)
        isleft = not isleft
        next += 1
    return root 

input = [1,2,3]
# print(minCameraCover(buildTree(input)))
input = [1,2,3,4,5,6,7] #[1,None,0,0]
input = [1,2,None,None,3,4,None,None,5]
# print(minCameraCover(buildTree(input)))
input = [1,None,2,3,None,None,4,5,None,None,6,7,None,8,9,10,11,12,13,14,15,None,16,17,None,None,18,19,None,20,None,21,None,None,22,23,None,24,None,25,26,27,None,28,None,None,29,30,None,31,32,None,33,None,34,None,35,None,36,37,38,39,40,41,42,None,43,44,45,None,46,None,47,48,49,50,None,51,None,None,52,53,54,None,55,None,56,None,57,None,58,None,59,60,61,None,0,None,0,0,None,0,None,0,0,None,0,0,0,0,None,0,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,0,0,0,None,0,0,None,None,0,None,0,None,0,None,0,None,0,None,0,0,None,None,0,None,0,0,0,0,None,0,0,0,None,0,0,None,0,None,0,0,None,0,None,0,0,0,None,None,0,0,None,0,None,0,None,0,0,0,None,None,0,0,None,0,0,0,0,0,0,0,None,0,0,0,0,0,0,None,0,None,0,None,0,None,0,0,None,None,0,0,0,0,None,0,0,None,0,None,0,None,0,0,None,0,None,None,0,None,0,0,None,0,0,0,0,0,None,0,0,0,0,None,0,None,0,0,None,0,None,None,0,0,None,None,0,0,0,0,0,0,0,None,0,None,0,0,None,None,0,0,None,None,0,0,None,0,None,None,0,0,0,None,0,0,None,0,0,None,0,None,0,None,0,0,None,0,None,0,0,0,0,None,0,0,0,0,0,0,None,0,0,0,0,0,None,0,None,0,None,None,0,0,None,None,0,0,0,None,0,0,0,0,0,None,0,0,0,0,0,None,0,0,0,None,0,None,0,0,0,None,0,0,None,0,None,0,0,0,0,0,0,None,0,None,0,0,None,0,None,0,None,0,0,None,0,None,0,0,0,0,None,0,None,0,0,0,None,0,0,0,0,0,None,0,None,0,0,0,None,0,0,0,0,None,0,0,0,None,0,None,0,0,0,0,0,0,None,0,0,0,None,0,None,None,0,None,0,0,0,None,0,0,0,0,0,0,0,0,0,0,0,None,0,0,0,0,None,0,0,None,0,0,0,0,0,None,0,0,None,None,0,0,None,None,0,None,0,0,None,0,0,0,0,0,None,0,0,0,None,0,None,0,None,0,None,0,None,0,None,0,0,0,None,0,0,None,0,0,None,None,0,0,0,None,0,0,None,0,None,0,None,0,None,0,0,0,None,0,None,0,None,None,0,0,0,None,0,0,None,None,0,0,None,0,None,0,None,0,None,0,0,0,0,0,None,None,0,0,0,None,0,0,0,None,0,None,0,None,0,0,None,0,0,None,0,None,0,0,0,0,0,0,None,None,0,None,0,None,0,None,0,0,0,None,0,0,None,0,0,None,0,0,0,0,None,None,0,None,0,0,0,None,0,0,None,0,None,0,0,0,0,0,None,None,0,None,0,0,0,0,0,0,None,0,None,0,0,None,0,0,None,0,None,0,0,None,0,0,0,0,0,0,0,0,None,0,None,None,0,0,None,0,0,0,None,None,0,0,None,None,0,None,0,0,None,0,0,None,0,None,0,0,None,0,0,0,0,0,0,0,0,None,0,0,None,0,0,0,0,0,0,0,0,0,None,0,None,None,0,0,0,0,None,None,0,0,0,0,None,0,None,0,None,0,None,None,0,0,0,0,None,0,None,0,0,0,None,0,0,None,0,None,0,0,0,0,None,None,0,0,None,None,0,None,0,0,0,0,0,None,0,0,0,0,None,None,0,0,0,None,0,0,None,0,None,None,0,None,0,0,0,0,0,0,0,None,0,None,0,None,0,0,None,0,None,0,0,0,0,None,0,0,None,0,0,0,0,None,0,0,0,0,0,0,None,None,0,0,None,None,0,0,None,0,0,0,0,0,None,None,0,0,None,0,0,0,0,0,0,0,0,None,0,0,None,0,0,None,0,0,0,0,None,None,0,None,0,None,0,None,0,0,0,None,0,None,0,0,0,0,None,0,0,0,None,0,None,None,0,0,0,None,0,0,None,None,0,0,None,0,None,None,0,0,None,None,0,0,None,None,0,None,0,0,None,0,None,0,None,0,0,0,None,None,0,0,None,0,None,None,0,0,0,0,0,0,0,None,0,None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,None,0,None,0,None,0,0,0,0,0,0,None,0,None,0,0,None,None,0,None,0,0,None,None,0,0,0,0,0,None,0,0,None,0,None,0,0,0,None,None,0,0,0,None,0,0,0,0,None,None,0,None,0,0,None,None,0,None,0,0,None,None,0,0,0,None,0,None,0,0,0,0,0,None,0,None,0,0,None,0,0,0,None,0,0,None,0,0,None,0,None,0,0,0,None,None,0,0,0,0,None,0,None,None,0,None,0,0,0,0,None,0,None,0,0,0,None,0,None,0,0,0,0,0,None,None,0,0,None,0,None,0,None,0,0,None,0,0,0,0,0,0,0,None,0,0,None,0,None,None,0,0,0,0,None,None,0,None,0,None,0,0,None,None,0,0,0,0,None,0,None,None,0,0,None,None,0,None,0]
print(minCameraCover(buildTree(input)))


#  approach 02 - using covered set - space: O(n)
def dfs02(root, parent, covered, cnt):
    Cnt = dfs02(root.left, root, covered, cnt)
    Cnt = dfs02(root.left, root, covered, cnt)
    ltCovered = root.left in covered 
    rtCovered = root.right in covered
    if parent == None and not root in covered or not ltCovered or not rtCovered :
        cnt += 1
        covered.add(root)
        covered.add(parent)
        covered.add(root.left)
        covered.add(root.right)
    return cnt
# covered=set([None]) 
# cnt = 0 
# dfs02(root,None,covered,cnt)    



# Recursive function that returns a list of three integers representing
# the minimum number of cameras needed for each state
def recurse(node):
    if not node:
        return [0, 0, float('inf')]

    L = recurse(node.left)
    R = recurse(node.right)

    leftCost = min(L[1], L[2])
    rightCost = min(R[1], R[2])

    dp0 = L[1] + R[1]
    dp1 = min(L[2] + rightCost, R[2] + leftCost)
    dp2 = 1 + min(L[0], leftCost) + min(R[0], rightCost)

    dp0 = min(dp0, float('inf'))
    dp1 = min(dp1, float('inf'))
    dp2 = min(dp2, float('inf'))

    return [dp0, dp1, dp2]

def minCameraCover_sol(root):
    res = recurse(root)
    return min(res[1], res[2])
