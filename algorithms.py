import math
from Problem import Problem
from ways import load_map_from_csv, compute_distance, info
from Node import Node
from main import huristic_function
from PriorityQueue import PriorityQueue


def ucs_rout(problem):
    def g(link):
        time = link.distance / max(info.SPEED_RANGES[link.highway_type]) / 1000
        return time
    return best_first_graph_search(problem, f=g)


def compute_route_time(route, graph):
    time = 0
    for i in range(len(route) - 1):
        source = graph.get_junction(route[i])
        target = graph.get_junction(route[i + 1])
        for link in source.links:
            if target.index == link.target:
                time += link.distance / max(info.SPEED_RANGES[link.highway_type]) / 1000
    return time


# This implementation is token from lecture 2.
def best_first_graph_search(problem, f):
    # create PriorityQueue
    frontier = PriorityQueue(lambda x: x.path_cost)
    frontier.append(Node(problem.s_start))
    closed_list = set()
    while frontier:
        # take out the minimum from top.
        node = frontier.pop()
        # if finish
        if problem.is_goal(node.state):
            return node.solution()
        # add it to close list.
        closed_list.add(node.state)
        # expand return all the possible actions.
        for child in node.expand(problem):
            # new child.
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            # has better path_cost
            elif child in frontier and f(problem.graph.get_link(node.state, child.state)) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None


def astar_route(source, target, graph):
    def g(link):
        time = link.distance / max(info.SPEED_RANGES[link.highway_type]) / 1000
        return time

    problem = Problem(source, target, graph)
    # TODO maybe change it
    junction_start = graph.get_junction(source)
    junction_end = graph.get_junction(target)
    lat1 = getattr(junction_start, "lat")
    lon1 = getattr(junction_start, "lon")
    lat2 = getattr(junction_end, "lat")
    lon2 = getattr(junction_end, "lon")
    return best_first_graph_search(problem, f=lambda n: g(n) + huristic_function(lat1, lon1, lat2, lon2))


def idastar_route(source, target, graph):
    def g(node):
        return node.path_cost

    problem = Problem(source, target, graph)
    junction_start = graph.get_junction(source)
    junction_end = graph.get_junction(target)
    lat1 = getattr(junction_start, "lat")
    lon1 = getattr(junction_start, "lon")
    lat2 = getattr(junction_end, "lat")
    lon2 = getattr(junction_end, "lon")

    return idastar_search(problem, f=lambda n: g(n) + huristic_function(lat1, lon1, lat2, lon2))


def idastar_search(problem, f):
    source = Node(problem.s_start)
    f_limit = f(source)
    next_f = math.inf
    while True:
        solution, f_limit = depth_limited_search(source, f_limit, next_f, f, problem)
        if solution:
            return solution
        if f_limit == math.inf:
            return None


def depth_limited_search(node, f_limit, next_f, f, problem):
    if f(node) > f_limit:
        return None, min(f(node), next_f)
    if problem.is_goal(node.state):
        return node.solution(), f_limit
    if node is None:
        pass
    for n in node.expand(problem):
        solution, new_f = depth_limited_search(n, f_limit, next_f, f, problem)
        if solution is not None:
            return solution, f_limit
        next_f = min(next_f, new_f)
    return None, next_f
