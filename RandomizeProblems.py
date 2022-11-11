from ways import load_map_from_csv
import random
import csv

NUMBER_OF_JUNCTIONS = 100
FILE_NAME = "problems.csv"
MIN_LENGTH = 5
MAX_LENGTH = 10


def create_random_list(roads):
    junctions = []
    number_of_junctions = len(roads)
    # get Random Junctions.
    for i in range(NUMBER_OF_JUNCTIONS):
        # get Random Starting junction.
        start_junction = roads[random.randint(0, number_of_junctions)]
        # get list of links.
        current_junction = start_junction
        limit = random.randint(MIN_LENGTH, MAX_LENGTH)
        for length in range(limit):
            links = list(getattr(current_junction, "links"))
            links_amount = len(links)
            if links_amount == 0:
                break
            # get Random one link.
            next_junction_id = links[random.randint(0, links_amount) - 1].target
            current_junction = roads[next_junction_id]
        line = str(start_junction.index) + ", " + str(current_junction.index)
        junctions.append(line)
    return junctions


def write_to_file(junctions):
    f = open(FILE_NAME, 'w')
    for junction in junctions:
        f.write("%s\n" % junction)
    f.close()


if __name__ == '__main__':
    roads = load_map_from_csv()
    junctions = create_random_list(roads)
    write_to_file(junctions)
