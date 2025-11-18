import heapq, math 

def max_score(nums, k):
  
    heap_list = []
    for num in nums:
        heapq.heappush(heap_list, -1*num)
    
    max_val = 0
    for trail in range(k):
        num = -1 * heapq.heappop(heap_list)
        max_val += num
        heapq.heappush(heap_list, -1*math.ceil(num/3))
    return max_val


print(max_score([10,20,30,40,50],4))
print(max_score([5,12,7,3,10],3))
print(max_score([6,9,15],2))