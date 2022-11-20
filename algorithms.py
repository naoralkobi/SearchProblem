import math
from Problem import Problem
from ways import load_map_from_csv, compute_distance, info
from Node import Node
from main import huristic_function
from PriorityQueue import PriorityQueue


def ucs_rout(problem):
    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)


def compute_route_time(route, graph):
    time = 0
    for i in range(len(route) - 1):
        link = graph.get_link(route[i], route[i + 1])
        distance_km = link.distance / 1000
        time = time + distance_km / max(info.SPEED_RANGES[link.highway_type])
    return time


# This implementation is token from lecture 2.
def best_first_graph_search(problem, f):
    # create PriorityQueue
    frontier = PriorityQueue(f)
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
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None


def astar_route(problem):
    def g(node):
        return node.path_cost

    def h(node):
        junction = problem.graph.get_junction(node.state)
        return huristic_function(junction.lat, junction.lon, problem.goal_junction.lat, problem.goal_junction.lon)

    return best_first_graph_search(problem, f=lambda n: g(n) + h(n))


def idastar_route(problem):
    def g(node):
        return node.path_cost

    def h(node):
        junction = problem.graph.get_junction(node.state)
        return huristic_function(junction.lat, junction.lon, problem.goal_junction.lat, problem.goal_junction.lon)

    return idastar_search(problem, f=lambda n: g(n) + h(n))


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
