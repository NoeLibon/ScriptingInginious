import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--input-csv', nargs='?')
parser.add_argument('-i', type=int, nargs='+')

args = parser.parse_args()

lines = []


def read_csv():
    with open(args.input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for index in args.i:
            for line in csv_reader:
                del line[int(index)]
                lines.append(line)


def write_csv():
    with open(args.input_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(lines)


if __name__ == '__main__':
    read_csv()
    write_csv()
