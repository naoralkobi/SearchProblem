import csv
from algorithms import ucs_rout, load_map_from_csv, compute_route_time

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
            route = ucs_rout(int(junction[0]), int(junction[1]), graph)
            print(route)
            time = compute_route_time(route, graph)
            print(time)
            # time = compute_route_time(route)
            file.write(str(route) + " - " + str(time) + "\r")
            # file.write('\r')
            # TODO remove this
            # break
    file.close()
