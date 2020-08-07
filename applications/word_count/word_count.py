import re

def word_count(s):
    # Your code here

# Case should be ignored. Output keys must be lowercase.
# Key order in the dictionary doesn't matter.
# Split the strings into words on any whitespace.
# Ignore each of the following characters:

    # Set the dictonary
    word_dict = {}
    # Convert to lower, strip the special chars and split the list
    lower_case = s.lower()
    new_list = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&]', '', lower_case)
    words = new_list.split()

    for word in words:
        # If the word is empty then move along
        if word == "":continue

        # If the word is already in the word dict, add one     
        if word in word_dict:
            word_dict[word] += 1
        # If not, add it
        else: 
            word_dict[word] = 1

    return word_dict
 
            

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))