def two_sum_less_than_k(nums, k):

    valid_list = []
    for num in nums:
        if num <= k-2:
            valid_list.append(num)
    
    max_sum = -1
    target = k-1
    if len(valid_list) > 1:
        valid_list.sort()
        lt, rt = 0, len(valid_list)-1
        while lt < rt:
            curr_sum = valid_list[lt] + valid_list[rt]
            if curr_sum > target:
                rt -= 1
            else:
                max_sum = max(max_sum, curr_sum)
                lt += 1
    return max_sum

# print(two_sum_less_than_k([2,1,3,3,5], 4))
# print(two_sum_less_than_k([8,4,9,2,10,1], 9))
# print(two_sum_less_than_k([3,4,5,8,6,2], 5))
# print(two_sum_less_than_k([4,4,4,4,4,4,4,4,4,4],12))

# Helper function to perform binary search
def search(nums, target, start):
    
    # Initialize pointers for binary search
    left, right = start, len(nums) - 1  
    result = -1

    # Perform binary search
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2  
        if nums[mid] < target:
            # Update result if nums[mid] is smaller than target
            result = mid  
             # Move left pointer to search for larger values
            left = mid + 1 
        else:
            # Move right pointer to search for smaller values
            right = mid - 1  

    # Return the index of the largest valid number that is less than target
    return result


def two_sum_less_than_k_sol(nums, k):
    maximum_sum = -1
    
    # Sort the array to facilitate binary search
    nums.sort()  

    # Iterate through the sorted array
    for i in range(len(nums)):
        # Calculate the target value which is k - nums[i] and find the largest j where nums[i] + nums[j] < k
        j = search(nums, k - nums[i], i + 1)  

        # If a valid pair is found (j > i), check if the sum is larger than the current maximum_sum
        if j > i:
            # Update the maximum_sum with the larger sum
            maximum_sum = max(maximum_sum, nums[i] + nums[j])  

    # Return the maximum sum found, or -1 if no valid pair exists
    return maximum_sum
