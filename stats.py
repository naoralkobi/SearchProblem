# Naor Alkobi 315679985
'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple, Counter
from ways import load_map_from_csv


def get_number_links(roads):
    length_links = []
    junctions = roads.junctions()
    for junction in junctions:
        length_links.append(len(getattr(junction, "links")))
    return length_links


def get_distance_links(roads):
    distance_links = []
    links = roads.iterlinks()
    for link in links:
        distance_links.append(getattr(link, "distance"))
    return distance_links


def get_counter(roads):
    links = roads.iterlinks()
    return Counter(getattr(link, "highway_type") for link in links)

def map_statistics(roads):
    """
    return a dictionary containing the desired information
    You can edit this function as you wish
    """
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    # return a list of junctions and count them.
    junction_amount = len(roads)
    links_amount = len(list(roads.iterlinks()))
    list_of_number_links = get_number_links(roads)
    list_of_distance_links = get_distance_links(roads)
    counter = get_counter(roads)
    histogram = dict(counter)

    return {
        'Number of junctions': junction_amount,
        'Number of links': links_amount,
        'Outgoing branching factor': Stat(max=max(list_of_number_links), min=min(list_of_number_links), avg=sum(list_of_number_links) / len(list_of_number_links)),
        'Link distance': Stat(max=max(list_of_distance_links), min=min(list_of_distance_links), avg=sum(list_of_distance_links) / len(list_of_distance_links)),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': histogram,  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
