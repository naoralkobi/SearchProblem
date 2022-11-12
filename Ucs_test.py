import csv
from main import ucs_rout
import ways
import os
FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "UCSRuns.txt"
ROOT_DIR = os.path.abspath(os.curdir)
roads = ways.graph.load_map_from_csv()

def compute_route_time(route):
    time = 0
    for i in range(len(route)-1):
        source = roads.get_junction(route[i])
        target = roads.get_junction(route[i+1])
        time += ways.tools.compute_distance(getattr(source, "lat"), getattr(source, "lon"),
                                            getattr(target, "lat"), getattr(target, "lon"))
        #print("time is: %s" % time)
    return time


if __name__ == '__main__':
    file = open(TEXT_FILE_NAME, "w")
    count = 0
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            route = ucs_rout(int(junction[0]), int(junction[1]))
            #print(route)
            time = compute_route_time(route)
            file.write(str(route) + " - " + str(time) + "\r")
            #file.write('\r')
            count += 1
            # TODO remove this
            break
    file.close()
