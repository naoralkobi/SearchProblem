import csv
from ways.draw import plot_path
from Problem import Problem
from algorithms import idastar_route
from ways import load_map_from_csv
import matplotlib.pyplot as plt
FILE_NAME = "10_problems.csv"
FOLDER_NAME = "solutions_img"


if __name__ == '__main__':
    graph = load_map_from_csv()
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            problem = Problem(int(junction[0]), int(junction[1]), graph)
            route = idastar_route(problem)
            fig = plt.gcf()
            plot_path(graph, route)
            plt.show()
            fig.savefig(FOLDER_NAME + '/solution' + '-' + junction[0] + '-' + junction[1], bbox_inches='tight')
            plt.close()

