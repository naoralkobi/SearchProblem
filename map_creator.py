# Naor Alkobi 315679985
import csv
from ways.draw import plot_path
import algorithms
import matplotlib.pyplot as plt
FILE_NAME = "10_problems.csv"
FOLDER_NAME = "solutions_img"


def main():
    graph = algorithms.load_map_from_csv()
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for junction in csv_reader:
            problem = algorithms.Problem(int(junction[0]), int(junction[1]), graph)
            route = algorithms.idastar_route(problem)
            fig = plt.gcf()
            plot_path(graph, route)
            plt.show()
            fig.savefig(FOLDER_NAME + '/solution' + '-' + junction[0] + '-' + junction[1], bbox_inches='tight')
            plt.close()


if __name__ == '__main__':
    main()


