from ways import graph
from ways.info import SPEED_RANGES


class Problem:
    """
    s_start - ID junction
    goal - ID junction
    """
    def __init__(self, s_start, goal, graph):
        self.s_start = s_start
        self.goal = goal
        self.graph = graph
        self.goal_junction = graph.get_junction(goal)

    def actions(self, s):
        return self.graph[s].links

    def succ(self, s, a):
        if a.source == s:
            return a.target
        raise ValueError(f'No route from {s} to {a}')

    def is_goal(self, s):
        return s == self.goal

    def step_cost(self, s, link):
        # KM / H
        return (link.distance / 1000) / SPEED_RANGES[link.highway_type][1]

    def state_str(self, s):
        return s

    def __repr__(self):
        return {'s_start': self.s_start, 'goal': self.goal, graph: 'self.G'}