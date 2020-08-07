import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# Split the words from the text and setup a word dict
split_words = words.split()
word_dict = {}

for i in range (len(split_words)):
    # If the word is not in the word dict then the dict is empty
    if split_words[i] not in word_dict:
        word_dict[split_words[i]] = []

# Append the split words into the dict
    try:
        word_dict[split_words[i]].append(split_words[i + 1])
    except IndexError:
        break

# TODO: construct 5 random sentences
# Your code here

# Punctuation to be aware of
punctuation = (".", "?", "!", '."', '?"', '!"')

def make_sentence(name):
    # Print a space after each name
    print(name, end=" ")

    # If the name ends with the punctuation defined then print new line
    if name.endswith(punctuation):
        print ('\n')
        return
    else:
         # If not then randomly choose words for the sentance 
        make_sentence(random.choice(word_dict[name]))

make_sentence("Alice")
make_sentence("Queen")
make_sentence("King")
make_sentence("One")
make_sentence("Dinah")


