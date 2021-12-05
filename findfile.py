from argparse import ArgumentParser

parser = ArgumentParser(description='find text file')
parser.add_argument('it', type=str)
arg = parser.parse_args()
with open(f'{arg.it}') as file:
    strings = file.readlines()
    for string in strings[:10]:
        print(string, end='')