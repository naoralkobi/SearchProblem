from Problem import Problem
from ways import load_map_from_csv, compute_distance
from Node import Node
from main import huristic_function
from PriorityQueue import PriorityQueue


def ucs_rout(source, target, graph):
    problem = Problem(source, target, graph)

    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)


def compute_route_time(route, graph):
    time = 0
    for i in range(len(route) - 1):
        source = graph.get_junction(route[i])
        target = graph.get_junction(route[i + 1])
        time += compute_distance(getattr(source, "lat"), getattr(source, "lon"),
                                 getattr(target, "lat"), getattr(target, "lon"))
        # print("time is: %s" % time)
    return str(route) + " - " + str(time)


def best_first_graph_search(problem, f):
    node = Node(problem.s_start)
    frontier = PriorityQueue(f)
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return compute_route_time(node.solution(), problem.graph)
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None


def astar_route(source, target):
    def g(node):
        return node.path_cost

    problem = Problem(source, target, load_map_from_csv())
    junction_start = problem.graph.get_junction(source)
    junction_end = problem.graph.get_junction(target)
    lat1 = getattr(junction_start, "lat")
    lat2 = getattr(junction_start, "lat")
    lon1 = getattr(junction_end, "lon")
    lon2 = getattr(junction_end, "lon")
    print("heuristic cost: ", huristic_function(lat1, lon1, lat2, lon2))
    return best_first_graph_search(problem, f=lambda n: g(n) + huristic_function(lat1, lon1, lat2, lon2))


def idastar_route(source, target):
    return None
