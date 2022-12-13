import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', nargs='?')
parser.add_argument('--output_file', nargs='?')
parser.add_argument('--filter_teacher', nargs='?')
parser.add_argument('--filter_good', nargs='?')
parser.add_argument('--order', action='store_true')
parser.add_argument('--select', nargs='?')

args = parser.parse_args()

with open(args.input_file, 'r') as input_file:
    json_content = input_file.read()
content = json.loads(json_content)


def main():
    filter_teacher()
    filter_good()
    order()
    select()
    with open(args.output_file, 'w') if args.output_file else open(args.input_file, 'w') as output_file:
        new_json_content = json.dumps(content, indent=2)
        output_file.write(new_json_content)


def filter_teacher():
    i = 0
    while i < len(content):
        if not args.filter_teacher:
            break
        if content[i]['Teacher'] != args.filter_teacher:
            del content[i]
            continue
        i += 1


def filter_good():
    i = 0
    while i < len(content):
        if not args.filter_good:
            break
        if float(content[i]['Grade']) < float(args.filter_good):
            del content[i]
            continue
        i += 1


def order():
    if args.order:
        content.sort(key=lambda student: student['Name'])


def select():
    i = 0
    while i < len(content):
        if not args.select:
            break
        selected_keys = args.select.split(',')
        keys = list(content[i])
        for key in keys:
            if key not in selected_keys:
                del content[i][key]
        i += 1


if __name__ == '__main__':
    main()
