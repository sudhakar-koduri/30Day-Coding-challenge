# Definition of a binary tree node
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(nums, st, end) -> TreeNode:
    if st > end or st < 0 or st >= len(nums):
        return None
    if st == end :
        return TreeNode(nums[st])
    mid = st + int((end -st)/2)
    root_node = TreeNode(nums[mid])
    root_node.left = build_tree(nums, st, mid-1)
    root_node.right = build_tree(nums, mid+1, end)
    return root_node

def sorted_array_to_bst(nums):
    if len(nums)==0:
        return None
    
    return build_tree(nums, 0, len(nums))

sorted_array_to_bst([11,22,33,44,55,66,77,88])
sorted_array_to_bst([25, 50, 75, 100, 125, 350])
sorted_array_to_bst([1, 2, 3])
sorted_array_to_bst([1, 2, 3, 4])
sorted_array_to_bst([-10, -3, 0, 5, 9],)
sorted_array_to_bst([1, 3])

def sorted_array_to_bst_helper_sol(nums, low, high):
    if(low > high):
        return None;

    mid = low + (high - low) //2 
    root = TreeNode(nums[mid])
    
    root.left = sorted_array_to_bst_helper_sol(nums, low, mid - 1)
    root.right = sorted_array_to_bst_helper_sol(nums, mid + 1, high)

    return root