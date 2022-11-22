import csv
import algorithms
from Problem import Problem
import time
FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "results/UCSRuns.txt"


def main():
    # open text file to write the results.
    file = open(TEXT_FILE_NAME, "w")
    graph = algorithms.load_map_from_csv()
    # loop each raw in CSV file.
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        time_counter = 0
        for junction in csv_reader:
            problem = Problem(int(junction[0]), int(junction[1]), graph)
            start = time.perf_counter()
            route, real_time = algorithms.ucs_rout(problem)
            time_counter = time_counter + time.perf_counter() - start
            # real_time = algorithms.compute_route_time(route, graph)
            list_to_string = str(route).strip('[]')
            line = list_to_string.replace(',', '') + " - " + str(format(real_time, ".4f")) + "\r"
            # print(line)
            file.write(line)
        avg_time = time_counter / 100
        avg_time = format(avg_time, ".4f")
        print(f'ucs test time: %s' % avg_time)
    file.close()


if __name__ == '__main__':
    main()

