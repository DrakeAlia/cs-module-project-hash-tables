nums = [ 4, 6, 10, 15, 16, ]

hashtable = {}

# for i, v in nums:
#     print(i)
#     print(v)


for ind, val in enumerate(nums):
    hashtable[val] = ind

    hashtable = { v:i for i, v in enumerate(nums)}

print(hashtable)
