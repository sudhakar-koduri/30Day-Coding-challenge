from collections import defaultdict
from queue import Queue
import copy

class DAG:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_node(self, u):
        self.adj[u]  # ensures key exists

    def add_edge(self, u, v):
        # Assuming caller guarantees acyclicity; add cycle checks if needed
        self.adj[u].append(v)
        # self.add_node(v)

    def adj_nodes(self, u):
        return self.adj[u]
    
    def dfs(self, start):
        visited = set()
        order = []
        def _dfs(u):
            visited.add(u)
            order.append(u)  # preorder; for postorder, append after children
            for w in self.adj[u]:
                if w not in visited:
                    _dfs(w)
        _dfs(start)
        return order

def loud_and_rich(richer, quiet):
    wealth_dag = DAG()
    quite_val = defaultdict()
    quite_order = defaultdict()
    head_list = []
    for idx, q_val in enumerate(quiet):
        wealth_dag.add_node(idx)
        quite_val[idx] = q_val
        quite_order[idx] = idx 
        head_list.append(idx)

    # Initialize in-degree map
    inDegree = {node: 0 for node in range(0,len(quiet))}

    for edge in richer:
        wealth_dag.add_edge(edge[1], edge[0])
        if edge[0] in head_list:
            head_list.remove(edge[0])
        inDegree[edge[0]] = inDegree[edge[0]] + 1

    for head in head_list:
        input_InDeg = copy.deepcopy(inDegree)
        # dfs_nodes = wealth_dag.dfs(head)
        # input_InDeg = {k: v for k, v in input_InDeg.items() if v != 0 and k in dfs_nodes}    
        queue = Queue()
        queue.put(head)
        traverse_order = []
        visited = []
        while queue.empty() == False:
            current = queue.get()
            traverse_order.append(current)
            for adj_idx in wealth_dag.adj_nodes(current):
                input_InDeg[adj_idx] = input_InDeg[adj_idx] - 1
                if input_InDeg[adj_idx] == 0:
                    queue.put(adj_idx)
                else:
                    visited.append(adj_idx)

            if queue.empty() :
                filtered_dict = {k: v for k, v in input_InDeg.items() if v != 0 and k in visited}
                if len(filtered_dict) > 0:
                    # for (k,v) in input_InDeg.items() if v > 0
                    k_min = min(filtered_dict, key=input_InDeg.get)
                    queue.put(k_min)
                    input_InDeg[k_min] = 0
        # traverse_order = wealth_dag.dfs(head)
        # print(head)
        # print(traverse_order)
        for x in reversed(traverse_order):
            for adj_idx in wealth_dag.adj_nodes(x):
              if quite_val[x] > quite_val[adj_idx]:
                quite_order[x] = quite_order[adj_idx]
                quite_val[x] = quite_val[adj_idx]

    return list(quite_order.values())

richer = [[3, 1],[4, 3],[2, 3],[2, 0]]
quiet = [3, 2, 4, 1, 0]

result = loud_and_rich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]] , [3,2,5,4,6,1,7,0])
print(result)
result = loud_and_rich([[15,21],[16,20],[7,17],[4,9],[3,13],[5,10],[8,9],[23,25],[0,5],[5,19],[3,22],[9,17],[11,14],[2,11],[0,23],[11,23],
                        [1,15],[1,24],[15,23],[6,20],[16,22],[7,19],[20,22],[5,12],[9,10],[0,7],[14,24],[3,24],[5,21],[17,23],[0,16],
                        [11,16],[1,8],[15,16],[6,13],[7,12],[15,25],[20,24],[12,20],[3,17],[5,14],[9,12],[5,23],[4,25],[9,21],[8,25],
                        [10,22],[13,21],[16,17],[7,14],[7,23],[18,23],[3,10],[5,7],[22,23],[21,25],[0,2],[5,16],[9,14],[5,25],[1,12],
                        [10,24],[16,19],[7,16],[3,12],[22,25],[12,24],[3,21],[9,16],[1,5],[19,20],[10,17],[1,14],[7,9],[24,25],[1,23],
                        [0,25],[16,21],[6,22],[20,21],[12,17],[5,11],[4,13],[3,23],[4,22],[8,13],[1,7],[2,6],[10,19],[6,15],[6,24],
                        [20,23],[4,6],[21,22],[3,16],[4,15],[3,25],[17,18],[10,12],[1,9],[8,24],[11,20],[2,17],[3,9],[20,25],[18,25],
                        [7,25],[12,21],[14,18],[5,6],[4,17],[1,2],[0,4],[17,20],[1,11],[0,13],[2,10],[1,20],[0,22],[6,10],[6,19],[7,18],
                        [12,14],[3,11],[4,10],[12,23],[4,19],[8,10],[1,4],[17,22],[8,19],[1,13],[0,15],[2,21],[6,12],[15,24],[3,4],[6,21],
                        [4,21],[8,12],[0,8],[17,24],[19,21],[8,21],[10,18],[2,14],[13,20],[15,17],[6,23],[4,5],[7,22],[0,1],[10,11],[0,10],
                        [5,24],[19,23],[9,22],[11,19],[13,22],[15,19],[6,25],[7,24],[4,7],[18,24],[21,23],[4,16],[5,8],[22,24],[14,20],
                        [5,17],[3,20],[0,3],[9,15],[0,12],[19,25],[2,18],[6,9],[7,8],[13,24]] , [1,19,12,5,20,4,8,10,18,14,23,17,6,9,16,24,21,13,3,2,7,15,22,11,0,25])
    #richer, quiet)
print(result)