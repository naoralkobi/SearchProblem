from Problem import Problem
from ways import load_map_from_csv
from Node import Node
from PriorityQueue import PriorityQueue


def ucs_rout(source, target):
    graph = load_map_from_csv()
    problem = Problem(source, target, graph)

    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)


def best_first_graph_search(problem, f):
    node = Node(problem.s_start)
    frontier = PriorityQueue(f)
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node.solution()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None
