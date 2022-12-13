import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text_file', type=str, nargs='?')

args = parser.parse_args()


def main():
    print(max(keep_num()))


def keep_num():
    with open(args.text_file) as file:
        text = file.read()
        split_text = text.split()
        numbers = []
        for i in split_text:
            try:
                if float(i):
                    if '.' in i:
                        numbers.append(float(i))
                    else:
                        numbers.append(int(i))
            except ValueError:
                pass
        return numbers


if __name__ == '__main__':
    main()
