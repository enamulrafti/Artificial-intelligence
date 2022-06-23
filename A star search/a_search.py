from queue import PriorityQueue
graph = [[0, 1, 4, 0, 0],
         [0, 0, 2, 5, 12],
         [0, 0, 0, 2, 0],
         [0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0]
         ]

nodes = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
Heu_cost = [7, 6, 2, 1, 0]


class TestClass:

    def __init__(self, Node_no, actual_cost, total_cost, prev_node_obj):
        self.Node_no = Node_no
        self.actual_cost = actual_cost
        self.total_cost = total_cost
        self.prev_node_obj = prev_node_obj


class TestClass1(object):
    def __init__(self, tcost, Tc_obj):
        self.tcost = tcost
        self.Tc_obj = Tc_obj

    def __lt__(self, other):
        return self.tcost <= other.tcost


q = PriorityQueue()

s = TestClass(0, 0, 7, None)
q.put(TestClass1(s.total_cost, s))

while not q.empty():
    next_item = q.get()
    obj = next_item.Tc_obj

    if obj.Node_no == 4:

        path = []
        path.append(obj.Node_no)
        while obj.Node_no != 0:
            obj = obj.prev_node_obj
            path.append(obj.Node_no)

        path.reverse()
        for i in path:
            print(nodes[i], end=' ')

        break

    x = graph[obj.Node_no]
    j = 0
    for a in x:
        if x[j] != 0:
            path_cost = obj.actual_cost + x[j]

            total = path_cost + Heu_cost[j]

            New_obj = TestClass(j, path_cost, total, obj)
            q.put(TestClass1(New_obj.total_cost, New_obj))

        j += 1
