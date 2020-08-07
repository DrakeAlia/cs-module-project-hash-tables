

# What General Problem Hash Tables Solve
# --------------------------------------
# They can look up things fast, in O(1) time.
# Applications
# ------------
# * In lieu of linear search.
# If the number of elements is small, it doesn't matter what data structure you use.
# * Memoization
#   * Caching
#   * Store the results of an expensive calculation so you don't have to recompute it later
# * Network cache
# * Indexing records
# * Removing duplicates
#   * Keys are unique
# * Counting things

# fib.py
# 0 1 1 2 3 5 8 13 21 34 ...
# cache = {}
# ​
# def fib(n):
# 	if n <= 1:
# 		return n
# ​
# 	if n not in cache:
# 		cache[n] = fib(n-1) + fib(n-2)
# ​
# 	return cache[n]
# ​
# print(f"{fib(999)}")
#for i in range(2000):
	#print(f"{i:3}: {fib(i)}")

# sorter.py
# d = {
#     "foo": 12,
#     "bar": 17,
#     "qux": 2
# }
# ​
# # Get items from hash table as tuples
# ​
# items = list(d.items())
# ​
# # Sort by key
# ​
# items.sort()
# #items.sort(reverse=True)
# ​
# print(items)
# ​
# # Sort by value
# ​
# #def fun1(e):
# #    return e[1]
# #
# #items.sort(key=fun1)
# ​
# items.sort(key=lambda e: e[1])
# ​
# print(items)

# letter_count.py
# def letter_count(s):
# ​
# 	d = {}
# ​
# 	for c in s:
# 		if c.isspace():
# 			continue
# ​
# 		c = c.lower()
# ​
# 		if c not in d:
# 			d[c] = 0
# ​
# 		d[c] += 1
# ​
# 	return d
# ​
# def print_sorted_letter_count(s):
# 	d = letter_count(s)
# ​
# 	items = list(d.items())
# ​
# 	items.sort(key=lambda e: e[1], reverse=True)
# ​
# 	for i in items:
# 		print(f"{i[0]}: {i[1]}")
# ​
# ​
# #print_sorted_letter_count("they also thought in the 1980s that there would be flying cars by 2015, from Back to the Future 2")
# ​
# print_sorted_letter_count("""For expensive operations, caching the results in a lookup table speeds future queries.
# The lookup table can be built in advance by iterating over all values in the domain of the function and recording the results.
# Or, more lazily, can be build as the individual values are passed in.
# Modify the code in this directory to build a lookup table so that it can finish running in under a minute.
# There's no test file for this. It's counting to 50,000, so if it finishes before you give up, then you're golden.""")


# caesar.py
# Caesar Cipher
# Hash table as a map between data values

"""
GOATS
JEHFN
"""

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

# Build the reverse map

for k, v in encode_table.items():
    decode_table[v] = k

def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

def decode(s):
    r = ""
    
    for c in s:
        r += decode_table[c]

    return r

print(encode("GOATS"))
print(encode("ELEPHANTS"))

print(decode("JEHFN"))
print(decode("OGOXDHCFN"))

# birthday.py
# import hashlib
# import random
# ​
# def hash_function(key):
#     return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff
# ​
# def how_many_before_collision(buckets, loops=1):
# ​
#     for i in range(loops):
#         tries = 0
#         tried = {}
# ​
#         while True:
#             random_key = random.random()
#             index = hash_function(random_key) % buckets
# ​
#             if index not in tried:
#                 tried[index] = 0
# ​
#             tried[index] += 1
#             tries += 1
# ​
#             if tried[index] == 10:
#                 break
# ​
#         print(f"{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}% full)")
# ​
# how_many_before_collision(65536, 10)