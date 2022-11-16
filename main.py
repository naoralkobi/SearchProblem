"""
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
"""

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
import algorithms


def huristic_function(lat1, lon1, lat2, lon2):
    max_speed = 110
    # calculate air distance / max speed.
    return algorithms.compute_distance(lat1, lon1, lat2, lon2) / max_speed


def find_ucs_rout(source, target):
    problem = algorithms.Problem(source, target, algorithms.load_map_from_csv())
    return algorithms.ucs_rout(problem)


def find_astar_route(source, target):
    return algorithms.astar_route(source, target, algorithms.load_map_from_csv())


def find_idastar_route(source, target):
    return algorithms.idastar_route(source, target, algorithms.load_map_from_csv())
    

def dispatch(argv):
    from sys import argv
    path = ""
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
