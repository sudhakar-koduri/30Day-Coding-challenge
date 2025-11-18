from collections import defaultdict

def can_finish(num_courses, prerequisites):
    depends_map = defaultdict(set)
    inDeg = [0] * num_courses

    for pre_req in prerequisites:
        depends_map[pre_req[1]].add(pre_req[0])
        inDeg[pre_req[0]] += 1
        if pre_req[0] not in depends_map:
           depends_map[pre_req[0]] = set()

    pending_q = []
    for i in range(num_courses):
        if inDeg[i] == 0:
            pending_q.append(i)

    visited = []
    while len(pending_q) > 0:
        u = pending_q.pop()
        visited.append(u)
        for v in depends_map[u]:
           inDeg[v] -= 1
           if inDeg[v] == 0:
              pending_q.append(v)

    return len(visited) == len(depends_map)

# print(can_finish(3,[[1,0],[2,1],[1,2]]))
# print(can_finish(4,[[1,0],[3,1],[1,2]]))
# print(can_finish(4,[[1,0],[3,1],[3,0],[1,2]]))
print(can_finish(4,[[1,0],[3,1],[0,3],[1,2]]))

# Using Kahn's alg.
from collections import deque
def can_finish_sol(num_courses, prerequisites):
    counter = 0
    if num_courses <= 0:
        return True

    inDegree = {i: 0 for i in range(num_courses)}
    graph = {i: [] for i in range(num_courses)}

    for edge in prerequisites:
        parent, child = edge[1], edge[0]
        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        course = sources.popleft()
        counter += 1
        for child in graph[course]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return counter == num_courses