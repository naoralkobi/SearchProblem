from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def ordered_set(self, coll):
        return dict.fromkeys(coll).keys()

    def children(self, roads, f):
        return [Node(link.target, self, self.path_cost + f(link)) for link in roads[self.state].links]


    def expand(self, problem):
        return self.ordered_set([self.child_node(problem, action) for action in problem.actions(self.state)])

    def child_node(self, problem, action):
        next_state = problem.succ(self.state, action)
        next_node = Node(next_state, self, action,
                         self.path_cost + problem.step_cost(self.state, action))
        return next_node

    def solution(self):
        return [node.state for node in self.path()]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state)