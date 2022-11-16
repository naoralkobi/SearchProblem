import csv
from ways.draw import plot_path
from Problem import Problem
from algorithms import idastar_route
from ways import load_map_from_csv
import matplotlib.pyplot as plt
FILE_NAME = "problems.csv"
FOLDER_NAME = "solutions_img"


if __name__ == '__main__':
    graph = load_map_from_csv()
    counter = 0
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            if counter == 10:
                break
            counter += 1
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

            fig = plt.gcf()
            plot_path(graph, route)
            plt.show()
            fig.savefig(FOLDER_NAME + '/solution-' + str(counter) + '-' + junction[0] + '-' + junction[1] + 'png', bbox_inches='tight')
            plt.close()

