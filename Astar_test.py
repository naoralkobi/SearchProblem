import csv
from Problem import Problem
import algorithms
import matplotlib.pyplot as plt
import time
FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "results/AStarRuns.txt"


def main():
    # open text file to write the results.
    file = open(TEXT_FILE_NAME, "w")
    heuristic_cost = []
    real_cost = []
    graph = algorithms.load_map_from_csv()
    # loop each raw in CSV file.
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        time_counter = 0
        for junction in csv_reader:
            problem = Problem(int(junction[0]), int(junction[1]), graph)
            start = time.perf_counter()
            route = algorithms.astar_route(problem)
            time_counter = time_counter + time.perf_counter() - start
            real_time = algorithms.compute_route_time(route, graph)
            lat1, lon1 = problem.graph.get_locations(problem.s_start)
            lat2, lon2 = problem.graph.get_locations(problem.goal)
            heuristic = algorithms.huristic_function(lat1, lon1, lat2, lon2)
            list_to_string = str(route).strip('[]')
            line = list_to_string.replace(',', '') + " - " + str(format(real_time, ".4f")) + " - " + str(format(heuristic, ".4f")) + "\r"
            print(line)
            heuristic_cost.append(heuristic)
            real_cost.append(real_time)
            file.write(line)
        avg_time = time_counter / 100
        avg_time = format(avg_time, ".4f")
        print(f'ASTAR test time: %s' % avg_time)
    file.close()
    # Draw the graph
    plt.plot(heuristic_cost, real_cost, 'o')
    plt.xlabel('heuristic cost')
    plt.ylabel('Real cost')
    plt.show()


if __name__ == '__main__':
    main()

