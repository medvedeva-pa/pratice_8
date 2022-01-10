import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
namespace = parser.parse_args()

with open(namespace.file_name) as file:
    reader = file.read()
    max_length = 0
    for word in reader.split():
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
    for word in reader.split():
        if len(word) == max_length:
            print(word)