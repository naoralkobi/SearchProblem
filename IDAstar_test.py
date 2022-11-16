import csv
from Node import Node
from Problem import Problem
from algorithms import huristic_function, idastar_route, compute_route_time
from ways import load_map_from_csv
import matplotlib.pyplot as plt
FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "results/IDAStarRuns.txt"


if __name__ == '__main__':
    file = open(TEXT_FILE_NAME, "w")
    graph = load_map_from_csv()
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            source = int(junction[0])
            target = int(junction[1])

            route = idastar_route(source, target, graph)
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
            print(line)
            file.write(line)

