# Problem 04: Single Element in a Sorted Array
# Statement: You are given a sorted array of integers, nums, where all integers appear twice except for one. Your task is to find and return the single integer that appears only once.
# The solution should have a time complexity of O(log n) or better and a space complexity of O(1).
# Constraints: 1≤ nums.length ≤ 1000; 	0≤ nums[i] ≤ 1000
def single_non_duplicate(nums):
   lt = 0
   rt = len(nums)-1
   while lt <= rt:
      if lt == rt:
         return nums[lt]
      
      mid = int((lt + rt  )/2)
      # check if mid is the target
      order = False
      isValid = (mid > 0 and nums[mid] == nums[mid-1])
      if (isValid and mid%2==1) :
         order = True
      if isValid == False:
        isValid = isValid or (mid < len(nums)-1) and nums[mid] == nums[mid+1]
        if (isValid and mid%2==0) :
          order = True
      if isValid == False:
        return nums[mid]

      if order:
         lt = mid+1  
      else:
         rt = mid - 1
   return -1

print(single_non_duplicate([1,1,2,2,3,3,4,4,5,5,6]))
print(single_non_duplicate([1, 2, 2, 3,3,4,4]))
print(single_non_duplicate([1, 1, 2, 2, 3, 4, 4]))
#0 1 2 3 4 5 6 7

def single_non_duplicate_sol(nums): 
    l = 0
    r = len(nums) - 1   # KEY : even and odd are treated as pairs; we navigate on even

    while l != r: 
        mid = l + (r - l) // 2

        if mid % 2 == 1: 
            mid -= 1 
        
        if nums[mid] == nums[mid + 1]: 
            l = mid + 2
        else :
            r = mid
        
    return nums[l]