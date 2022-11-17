import csv
from Problem import Problem
from algorithms import load_map_from_csv, astar_route, compute_route_time, huristic_function
import matplotlib.pyplot as plt
import time
import re

FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "results/AStarRuns.txt"


if __name__ == '__main__':
    # open text file to write the results.
    file = open(TEXT_FILE_NAME, "w")
    heuristic_cost = []
    real_cost = []
    graph = load_map_from_csv()
    # loop each raw in CSV file.
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        time_counter = 0
        for junction in csv_reader:
            source = int(junction[0])
            target = int(junction[1])
            start = time.perf_counter()
            route = astar_route(source, target, graph)
            time_counter = time_counter + time.perf_counter() - start
            real_time = compute_route_time(route, graph)
            problem = Problem(source, target, graph)

            junction_start = graph.get_junction(source)
            junction_end = graph.get_junction(target)

            lat1 = getattr(junction_start, "lat")
            lon1 = getattr(junction_start, "lon")
            lat2 = getattr(junction_end, "lat")
            lon2 = getattr(junction_end, "lon")
            list_to_string = str(route).strip('[]')
            heuristic = huristic_function(lat1, lon1, lat2, lon2)
            line = list_to_string.replace(',', '') + " - " + str(real_time) + " - " + str(heuristic) + "\r"
            print(line)
            heuristic_cost.append(heuristic)
            real_cost.append(real_time)
            file.write(line)
        print(f'ASTAR test time: {time_counter / 100}')
    file.close()
    # Draw the graph
    plt.plot(heuristic_cost, real_cost, 'o')
    plt.xlabel('heuristic cost')
    plt.ylabel('Real cost')
    plt.show()

