import math 

def minEatingSpeed(piles, h):
    sum_n = sum(piles)
    avg_n = math.ceil(sum_n/ h)
    minSpeed = avg_n

    hrSpend = 0
    for x in piles:
        hrSpend = hrSpend + math.ceil(x/minSpeed)
    while hrSpend > h:
        hrSpend = 0
        minSpeed = minSpeed + 1
        for x in piles:
            hrSpend = hrSpend + math.ceil(x/minSpeed)
    return minSpeed

print(minEatingSpeed([1,2,3],5))
print(minEatingSpeed([4,4,4,4], 8))
print(minEatingSpeed([9,1,15,7], 5))
print(minEatingSpeed([5,8,6,4,3,9,2,7], 50))

# The solution speed lies between 1 to max(piles) since h > len(piles)
# Hence, Redefine the problem into binary search to check for the min hour in this range
def minEatingSpeed_sol(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid  # ceiling division
        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left