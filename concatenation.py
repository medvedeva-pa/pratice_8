import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_names', nargs='+')

concatenation = ''
for i in parser.parse_args().file_names:
    with open(i) as file:
        concatenation += file.read()
print(concatenation)