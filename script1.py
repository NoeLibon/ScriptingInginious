import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integers', type=int, nargs='+')

args = parser.parse_args()


def main():
    print(sum(args.integers))


if __name__ == '__main__':
    main()
