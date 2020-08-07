# lookup.py

# import math
# ​
# lookup_table = {}
# ​
# for n in range(1, 1001):  # O(n)
#     lookup_table[n] = 1 / math.sqrt(n)
# ​
# def inv_sqrt(n):
#     """n is an integer between 1 and 1000"""
# ​
#     #return 1 / math.sqrt(n)
#     return lookup_table[n]
# ​
# ​
# print(inv_sqrt(10))
# print(inv_sqrt(100))


# lookup_lazy.py

# import math
# ​
# lookup_table = {}
# ​
# def inv_sqrt(n):
#     """n is an integer between 1 and 1000"""
# ​
#     # Lazily build lookup table
# ​
#     if n not in lookup_table:
#         lookup_table[n] = 1 / math.sqrt(n)
# ​
#     return lookup_table[n]
# ​
# ​
# print(inv_sqrt(10))
# print(inv_sqrt(100))
# ​

# index.py

# records = [
#     ("Alice", "Engineering"),
#     ("Bob", "Sales"),
#     ("Carol", "Sales"),
#     ("Dave", "Engineering"),
#     ("Erin", "Engineering"),
#     ("Frank", "Engineering"),
#     ("Grace", "Marketing"),
# ]
# ​
# """
# dept_idx = {
#     "Sales": ['Bob', 'Carol'],
#     "Marketing": ['Grace'],
#     "Engineering": ['...']
# }
# """
# ​
# dept_idx = {}
# ​
# # Build index by dept
# for name, dept in records:  # O(n) over number records
# ​
#     if dept not in dept_idx:
#         dept_idx[dept] = []
# ​
#     dept_idx[dept].append(name)
# ​
# # Which employees are in a given department?
# ​
# def emp_by_dept(d):
#     """
#     emp = []
# ​
#     for name, dept in records: # O(n)
#         if dept == d:
#             emp.append(name)
# ​
#     return emp
#     """
# ​
#     return dept_idx[d]  # O(1)
# ​
# def add_employee(name, dept):
#     records.append((name, dept))
# ​
#     if dept not in dept_idx:
#         dept_idx[dept] = []
# ​
#     dept_idx[dept].append(name)
# ​
# print(emp_by_dept("Sales"))
# ​
# add_employee('Hank', 'Marketing')
# ​
# print(emp_by_dept("Marketing"))

# webcache.py

# """
# Command line program that repeatedly accepts URL as input, and prints out the
# HTML data as output.
# ​
# TODO: add caching.
# """
# ​
# import datetime
# import urllib.request
# ​
# class CacheEntry:
#     def __init__(self, url, data):
#         self.url = url
#         self.data = data
#         self.timestamp = datetime.datetime.now().timestamp()
# ​
# cache = {}  # Key is the URL, the value is the data from that URL
# ​
# TIMEOUT_SECONDS = 10
# ​
# while True:
#     url = input("Enter a URL: ")
# ​
#     if url == 'exit':
#         break
# ​
#     needs_refresh = False
# ​
#     if url not in cache:
#         needs_refresh = True
#     else:
#         # Did it timeout?
#         cur_time = datetime.datetime.now().timestamp()
#         diff_time = cur_time - cache[url].timestamp
# ​
#         """
#         if diff_time > TIMEOUT_SECONDS:
#             needs_refresh = True
#         # ^^ same as single line, below
#         """
# ​
#         needs_refresh = diff_time > TIMEOUT_SECONDS
# ​
#     if needs_refresh:
#         print("GETTING FROM SERVER")
#         resp = urllib.request.urlopen(url)
#         data = resp.read()
# ​
#         cache[url] = CacheEntry(url, data)
# ​
#     print(cache[url].data[:60])
