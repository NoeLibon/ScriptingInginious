import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', default='.', nargs='?')
parser.add_argument('--output-dir', default='.', nargs='?')

args = parser.parse_args()


def main():
    content = os.listdir(args.input_dir)
    for i in content:
        if '.' in i:
            extension = i.split('.')[-1]
            if extension:
                if extension not in os.listdir(args.output_dir):
                    os.mkdir(args.output_dir + '/' + extension)
                shutil.move(args.input_dir + '/' + i, args.output_dir + '/' + extension + '/' + i)


if __name__ == '__main__':
    main()
