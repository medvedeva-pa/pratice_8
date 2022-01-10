import random

with open('passwords.txt') as passwords:
    reader = passwords.read()
    words_set = reader.split(', ')
    word1 = random.choice(words_set)
    for n, i in enumerate(words_set):
        if i == word1:
            words_set.pop(n)
            break
    word2 = random.choice(words_set)
    word1 = word1.capitalize()
    word2 = word2.capitalize()
    password = word1 + word2
    print(password)