"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# Set addition and subtraction dicts
addition = {}
subtraction = {}

for i in range(0, len(q)):
    for j in range(0, len(q)):
        addition[f'f({q[i]}) + f({q[j]})'] = f(q[i]) + f(q[j])
        # print('add',f(q[i]) + f(q[j]))
        # print('subtract',f(q[i]) - f(q[j]))
        subtraction[f'f({q[j]}) - f({q[i]})'] = f(q[j]) - f(q[i])

for add in addition:
    for sub in subtraction:
        if subtraction[sub] == addition[add]:
            print(f'{add} = {sub} = {addition[add]}')


# Other method:
# looping through each of the combinations

# def print_combinations1(set):
#     output = ""

#     for a in set:
#         for b in set:
#             for c in set:
#                 for d in set:
#                     if f(a) + f(b) == f(c) - f(d):
#                         output += f"f({a}) + f({b}) = f({c}) - f({d})\n"

#     print(output.count('\n'))


# # store the results of summing in a dictionary
# # Then check against this dictionary with the diffs

# def print_combinations2(input_set):
#     sums = {}

#     output = ""

#     f_lut = {}

#     for num in input_set:
#         f_lut[num] = f(num)

#     for a in input_set:
#         for b in input_set:

#             sum = f_lut[a] + f_lut[b]

#             if sum not in sums:
#                 sums[sum] = [(a, b)]
#             else:
#                 sums[sum].append((a, b))

#     for c in input_set:
#         for d in input_set:
#             diff = f_lut[c] - f_lut[d]
#             if diff in sums:
#                 for sum in sums[diff]:
#                     output += f"f({sum[0]}) + f({sum[1]}) = f({c}) - f({d})\n"

#     print(output.count('\n'))


# import time

# q = set(range(-20, 20))

# start_time1 = time.time()
# print_combinations1(q)
# end_time1 = time.time()

# start_time2 = time.time()
# print_combinations2(q)
# end_time2 = time.time()

# print(f"Combinations 1 finished in {end_time1 - start_time1}")
# print(f"Combinations 2 finished in {end_time2 - start_time2}")