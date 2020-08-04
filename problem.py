# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:

object = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# Your algorithm should return 41, the sum of the values 23 and 18.
# int total as 0
# start with for loop over our objects
# filter/checking over the values that contain only numbers, using conditionals (if statements)
# add number to total
# print total 

total = 0
for key in object:
    # print(object[key])
    if type(object[key]) is int:
        total += object[key]
print (total)
