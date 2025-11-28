import heapq
def connect_sticks(sticks):
  
    heapq.heapify(sticks)
    min_cost = 0
    while len(sticks) > 1:
        cost = heapq.heappop(sticks) + heapq.heappop(sticks)
        heapq.heappush(sticks, cost)
        min_cost += cost
    return min_cost

sticks = [1,10,3,3,3]
print(connect_sticks(sticks))