def isFeasible(batteries, n, val):
    return int(sum([ min(x,val) for x in batteries]) / n) >= val

def maxRunTime(batteries, n):
    
    if len(batteries) < n:
        return 0

    min_range = min(batteries)
    max_range = int(sum(batteries) / n)

    result = 0
    while min_range <= max_range:
        mid = min_range + (max_range - min_range)//2
        if isFeasible(batteries, n, mid):
            result = max(result,mid)
            min_range = mid + 1
        else:
            max_range = mid - 1

    return result

# print(maxRunTime([2,3,3,4],3))
print(maxRunTime([2,2,3,5],3))
print(maxRunTime([1,1,4,5],2))
print(maxRunTime([2,2,2,2],1))

def maxRunTime_sol(batteries, n):
  total_power = sum(batteries)
  left, right = 0, total_power // n

  while left < right:
    mid = right - (right - left) // 2
    usable = sum(min(b, mid) for b in batteries)

    if usable >= mid * n:
      left = mid
    else:
      right = mid - 1

  return left