import csv
from algorithms import ucs_rout, load_map_from_csv, compute_route_time, Problem

FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "results/UCSRuns.txt"


if __name__ == '__main__':
    # open text file to write the results.
    file = open(TEXT_FILE_NAME, "w")
    graph = load_map_from_csv()
    # loop each raw in CSV file.
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            problem = Problem(int(junction[0]), int(junction[1]), graph)
            route = ucs_rout(problem)
            time = compute_route_time(route, graph)
            list_to_string = str(route).strip('[]')
            line = list_to_string.replace(',', '') + " - " + str(time) + "\r"
            print(line)
            file.write(line)
    file.close()
