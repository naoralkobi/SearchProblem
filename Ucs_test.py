import csv
from algorithms import ucs_rout, load_map_from_csv
import os

FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "UCSRuns.txt"
ROOT_DIR = os.path.abspath(os.curdir)


if __name__ == '__main__':
    # open text file to write the results.
    file = open(TEXT_FILE_NAME, "w")
    graph = load_map_from_csv()
    # loop each raw in CSV file.
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            route_and_time = ucs_rout(int(junction[0]), int(junction[1]), graph)
            # TODO remove this
            print(route_and_time)
            # time = compute_route_time(route)
            file.write(str(route_and_time) + " - " + "\r")
            # file.write('\r')
            # TODO remove this
            # break
    file.close()
