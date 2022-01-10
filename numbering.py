import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
file_name = parser.parse_args().file_name

with open(input('File name: '), 'w') as export_file:
    with open(file_name) as import_file:
        input_lines = ''
        for n, line in enumerate(import_file.readlines()):
            input_lines += f'{n}: {line}'
        export_file.write(input_lines)