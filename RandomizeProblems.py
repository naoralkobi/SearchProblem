from ways import load_map_from_csv
import random
import csv

NUMBER_OF_JUNCTIONS = 100
FILE_NAME = "problems.csv"
MIN_LENGTH = 5
MAX_LENGTH = 15
LIMIT = 100


def create_random_list(roads):
    junctions = []
    number_of_junctions = len(roads)

    # create LIMIT=100 problems.
    for i in range(LIMIT):
        # get Random Starting junction.
        start_index = random.randint(0, number_of_junctions-1)
        links_amount = len(roads.junctions()[start_index].links)
        # make sure the first junction has few links.
        while links_amount == 0:
            start_index = random.randint(0, number_of_junctions-1)

        end_index = start_index
        current_index = start_index
        loop_number = random.randint(MIN_LENGTH, MAX_LENGTH)

        for loop_counter in range(loop_number):

            last_current_index = current_index
            current_index = end_index

            if_random = 0
            help_index = end_index

            number_of_links = len(roads.junctions()[end_index].links)
            for link_index in range(number_of_links):

                if if_random == 0:
                    help_index = roads.junctions()[help_index].links[
                        random.randint(0, len(roads.junctions()[help_index].links) - 1)].target
                else:
                    help_index = roads.junctions()[help_index].links[link_index].target

                if help_index != last_current_index:
                    end_index = help_index
                    break
                else:
                    if if_random == 0:
                        if_random = 1
                    help_index = end_index
            # if end_junction dont have more links.
            if len(roads.junctions()[end_index].links) == 0:
                break

        if start_index == end_index:
            end_index = roads.junctions()[start_index].links[0].target
        line = str(start_index) + ", " + str(end_index)
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
