def countSubarrays(nums, minK, maxK):

    lt = 0
    curr_min = -1
    curr_max = -1
    bounded_arr_cnt = 0
    last_bound_cnt = 0
    for rt, num in enumerate(nums):
        # Check the num is in bound
        if num < minK or num > maxK:
            curr_min = curr_max = -1
            last_bound_cnt = 0
            lt = rt+1
        if num > minK and num < maxK :
            bounded_arr_cnt += last_bound_cnt

        if num == minK and num == maxK:
            curr_min = curr_max = rt 
            last_bound_cnt = rt - lt +1
            bounded_arr_cnt += last_bound_cnt
        else:    
            if num == minK:
                curr_min = rt
                if curr_max >= 0:
                    last_bound_cnt = curr_max - lt +1
                    bounded_arr_cnt += last_bound_cnt
            if num == maxK:
                curr_max = rt
                if curr_min >= 0:
                    last_bound_cnt = curr_min - lt + 1
                    bounded_arr_cnt += last_bound_cnt

    return bounded_arr_cnt

print(countSubarrays([2,1,4,3,2],2,4))
print(countSubarrays([1,2,3,2,1],1,3))
print(countSubarrays([4,4,4],4,4))
print(countSubarrays([2,2,2],4,4))

def countSubarrays_sol(nums, minK, maxK):
    n = len(nums)
    min_pos = max_pos = left_bound = -1
    count = 0

    for i in range(n):
        if nums[i] < minK or nums[i] > maxK:
            left_bound = i
            min_pos = max_pos = -1

        if nums[i] == minK:
            min_pos = i

        if nums[i] == maxK:
            max_pos = i

        if min_pos != -1 and max_pos != -1:
            count += max(0, min(min_pos, max_pos) - left_bound)

    return count