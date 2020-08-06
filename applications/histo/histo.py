import re
# Your code here

# Import the text
with open("robin.txt") as f:
    words = f.read()

# Convert to lower, strip the special chars and split the list   
lower_case = words.lower()
new_list = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&]', '', lower_case)
new_words = new_list.split()

# Set the histogram dict
histogram = {}

for word in new_words:
    # If word is not in histogram, add it
    if words not in histogram:
        histogram[word] = "#"
    # If it is, add one
    else:
        histogram[word] += "#"

# List the items in histogram dict
word_occurrence = list(histogram.items())
# Using the lambda expression, sort by key and list it in reverse
word_occurrence.sort(key=lambda x: x[1], reverse=True)

for (key, value) in word_occurrence:
    print(f'{key} : {value}') 
