import csv
import time
from Problem import Problem
from algorithms import huristic_function, idastar_route
from ways import load_map_from_csv
FILE_NAME = "10_problems.csv"
TEXT_FILE_NAME = "results/IDAStarRuns.txt"


if __name__ == '__main__':
    file = open(TEXT_FILE_NAME, "w")
    graph = load_map_from_csv()
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        start = time.perf_counter()
        time_counter = 0
        for junction in csv_reader:
            problem = Problem(int(junction[0]), int(junction[1]), graph)
            start = time.perf_counter()
            route = idastar_route(problem)
            time_counter = time_counter + time.perf_counter() - start

            lat1, lon1 = problem.graph.get_locations(problem.s_start)
            lat2, lon2 = problem.graph.get_locations(problem.goal)

            heuristic = huristic_function(lat1, lon1, lat2, lon2)
            list_to_string = str(route).strip('[]')

            line = list_to_string.replace(',', '') + " - " + str(heuristic) + "\r"
            print(line)
            file.write(line)
        print(f'ID ASTAR test time: {time_counter / 10}')
    file.close()

