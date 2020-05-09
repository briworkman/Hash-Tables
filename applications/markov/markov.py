import random
import re
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# TODO: construct 5 random sentences

word_dict = {}
words = words.split()
for i, word in enumerate(words[:-1]):
    if word in word_dict:
        word_dict[word] = word_dict[word] + [words[i + 1]]
    else:
        word_dict[word] = [words[i + 1]]
start_words = []
stop_words = []
pattern_one = '[A-Z]+[a-z]'
pattern_two = '["]+[A-Z]+[a-z]'
pattern_three = '[.?!]$'
pattern_four = '[.?!]+["]$'

for key in word_dict:
    if re.search(pattern_one, key) or re.search(pattern_two, key):
        start_words.append(key)
    if re.search(pattern_three, key) or re.search(pattern_four, key):
        stop_words.append(key)


def print_sentence():
    stop = False
    word = random.choice(start_words)
    sentence = word
    if word in stop_words:
        return sentence
    while stop is False:
        word = random.choice(word_dict[word])
        sentence = sentence + " " + word
        if word in stop_words:
            stop = True
    return sentence


print("ONE", print_sentence())
print("TWO", print_sentence())
print("THREE", print_sentence())
print("FOUR", print_sentence())
print("FIVE", print_sentence())
