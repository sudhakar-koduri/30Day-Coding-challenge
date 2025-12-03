
def contains_nearby_duplicate(nums, k):
    num_idx = {}
    for idx,n in enumerate(nums):
        if n in num_idx:
            if idx - num_idx[n] <= k:
                return True
                #Else Save the latest index to check if the next occurance falls within the valid range
        num_idx[n] = idx
    # Replace this placeholder return statement with your code
    return False