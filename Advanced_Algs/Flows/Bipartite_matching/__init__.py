# python3
# python3
import queue
from copy import deepcopy
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.

class FlowGraph:
    def __init__(self, n, f):
        self. flights = f
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    flight_count, crew_count = map(int, input().split())
    graph = FlowGraph(flight_count + crew_count + 2,flight_count ) #plus 2 for the first and last nodes
    last_node=  crew_count + flight_count + 1
    for _ in range(flight_count):
        graph.add_edge(0 ,_ + 1, 1)
    for _ in range(flight_count):
        crews   = input().split()
        for i in range(len(crews)):
            if crews[i] == "1":
                graph.add_edge(_ + 1 , flight_count+ i + 1, 1)
    for _ in range(crew_count):
        graph.add_edge(flight_count + _ +1, last_node, 1)
    return graph

def Find_path(Gf,from_ ,target):
    Q = queue.Queue()
    Q.put(from_)
    path = []
    visited = [-1 for _ in range(len(Gf.graph))]
    visited[from_] = -2
    while Q.qsize() >0:
        origin = Q.get()
        for id in Gf.get_ids(origin):
            edge = Gf.get_edge(id)
            if edge.capacity - edge.flow == 0:
                continue
            if edge.v == edge.u or edge.v == 0 :
                continue
            if visited[edge.v] == -1:
                Q.put(edge.v)
                visited[edge.v] = id
                if edge.v == target:
                    prev_id = id
                    while prev_id != -2:
                        path.append(prev_id)
                        prev_id = visited[Gf.get_edge(prev_id).u]
                    return path
    return False


def max_flow(graph, from_, to ):
    flow = 0
    crew_in_flight = ["-1 "]*graph.flights
    while True:
        #find shortes path of edges as ids, return False if no valid path
        path = Find_path(graph, from_,to) #return [shortest patth as edges]
        if path  == False:
            return "".join(crew_in_flight)
        ##find the bottleneck
        bottle_neck = 10001
        for edge in path:
            e = graph.get_edge(edge)
            if e.capacity - e.flow < bottle_neck:
                bottle_neck = e.capacity - e.flow
        ##update the edges
        for id in path:
            graph.add_flow(id, bottle_neck)
        path.pop()
        #update the crews
        for i in range(1,len(path), 2):
            flight =  graph.edges[path[i]].u -1
            crew = graph.edges[path[i]].v  - graph.flights
            crew_in_flight[flight] = str(crew) + " "
        #update the flow
        flow += bottle_neck


if __name__ == '__main__':
    graph = read_data()
    '''
    i  = 0
    for edge in graph.edges:
        i +=1
        if  i == 2:
            i = 0
        else:
            print(edge.u, edge.v)
    '''
    print(max_flow(graph, 0, graph.size() - 1)[:-1])