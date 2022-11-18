import csv
import time

from Node import Node
from Problem import Problem
from algorithms import huristic_function, idastar_route, compute_route_time
from ways import load_map_from_csv
import matplotlib.pyplot as plt
FILE_NAME = "5_problems.csv"
TEXT_FILE_NAME = "results/IDAStarRuns.txt"


if __name__ == '__main__':
    file = open(TEXT_FILE_NAME, "w")
    graph = load_map_from_csv()
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        start = time.perf_counter()
        time_counter = 0
        for junction in csv_reader:
            source = int(junction[0])
            target = int(junction[1])
            start = time.perf_counter()
            route = idastar_route(source, target, graph)
            time_counter = time_counter + time.perf_counter() - start
            problem = Problem(source, target, graph)

            junction_start = graph.get_junction(source)
            junction_end = graph.get_junction(target)

            lat1 = getattr(junction_start, "lat")
            lon1 = getattr(junction_start, "lon")
            lat2 = getattr(junction_end, "lat")
            lon2 = getattr(junction_end, "lon")

            heuristic = huristic_function(lat1, lon1, lat2, lon2)
            list_to_string = str(route).strip('[]')

            line = list_to_string.replace(',', '') + " - " + str(heuristic) + "\r"
            # print(line)
            file.write(line)
        # print(f'ID ASTAR test time: {time_counter / 5}')
    file.close()

