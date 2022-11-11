import csv
from main import ucs_rout
import os
FILE_NAME = "problems.csv"
TEXT_FILE_NAME = "UCSRuns.txt"

ROOT_DIR = os.path.abspath(os.curdir)


if __name__ == '__main__':
    file = open(TEXT_FILE_NAME, "w")
    count = 0
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            route = ucs_rout(int(row[0]), int(row[1]))
            print(route)
            file.write(str(route))
            file.write('\r')
            count += 1
            break

    file.close()
