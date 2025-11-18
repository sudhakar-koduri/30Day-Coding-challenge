import sys

# Problem: Maximum Product Subarray
# Statement: Given an integer array, nums, find a subarray that has the largest product, and return the product.
# Constraints: 1≤ nums.length ≤ 1000; −10≤ nums[i] ≤10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32−bit integer.
def max_product(nums):

    nums.append(0)
    curr_max = 1
    max_val = -sys.maxsize - 1
    neg_max_val = -sys.maxsize - 1
    neg_max_idx = -1
    st_idx = 0
    for idx, val in enumerate(nums):
        if val > 0:
           curr_max = curr_max * val
        elif val == 0:
            if st_idx == idx:
                max_val = max(max_val, 0)
            elif curr_max >= 0:
                max_val = max(max_val, curr_max)
            elif neg_max_idx > -1:
                max_val = max(max_val, int(curr_max / neg_max_val))
                if max_val == 1 :
                    max_val = max(nums[0:idx]) 
            else:
                max_val = curr_max
            curr_max = 1
            neg_max_val = -sys.maxsize - 1
            neg_max_idx = -1
            st_idx = idx + 1
        else:
            if curr_max > 0:
                max_val = max(max_val, curr_max)
            curr_max = curr_max * val
            if curr_max < 0 and curr_max > neg_max_val:
                neg_max_idx = idx 
                neg_max_val = curr_max
    
    return max_val

print(max_product([-5,-10,2,9,-7,9,7,-2,-7,-10,0,-1,-5,10,0,7,1,-4,2,5,-7,9,8,2,0,-9,-1,10,-3,10,5,9,0,3,9,2,-10,2,1,6,-6,6,-8,5,5,2,5,-4,0,0,8,10,-4,3,-1,5,3,0,6,10,-6,8,-2,2,-1,6,9,-5,4,7,-1,2,0,-7,-5,0,6,0,-4,-8,-2,4,-5,-5,-10,0,-2,6,-10,-9,7,2,-5,-2,1,5,4,-7,5,-5]))
# print(max_product([0]))
# print(max_product([2, -5, 3, 1, -4, 0, -10, 2]))
# print(max_product([-2,0,-1]))
# print(max_product([2,3,-2,4]))
# print(max_product([1,2,3,4]))

def max_product_sol(nums):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]

        prev_max_so_far = max_so_far
        max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, prev_max_so_far * curr, min_so_far * curr)

        result = max(max_so_far, result)

    return result