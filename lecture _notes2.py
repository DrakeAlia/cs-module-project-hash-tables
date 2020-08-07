# Collision resolution notes

# Collision resolution by chaining
# --------------------------------
# Make our array of slots into an array of linked lists.
# Each linked list node is a HashTableEntry.
# Put
# ---
# Slot
# Index Chain (linked list)
# ----- -------------------------------
#  0    -> None
#  1    {foo:12} -> None
#  2    {baz:999} -> {bar:50} -> None
#  3    -> None
# put("foo", 12)   # hashes to 1
# put("bar", 30)   # hashes to 2
# put("baz", 999)  # hashes to 2 -- collision
# put("bar", 50)   # hashes to 2 -- collision
# 1. Figure out the index
# 2. Search the linked list to see if the key is there
# 2a. If the key is there, overwrite the value
# 2b. If not there, create a new HashTableEntry and insert it in the list
# Get
# ---
# 1. Figure out the index for the key
# 2. Search the linked list at the index for the HashTableEntry that matches the key
# 3. Return the value for the entry, or None if not found
# Delete
# ------
# 1. Figure out the index for the key
# 2. Search the linked list at the index for the HashTableEntry that matches the key
# 2a. If found, delete the entry from the linked list--return the value
# 2b. If not found, return None


# list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f'Node({repr(self.value)})'
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        """Print entire linked list."""
        if self.head is None:
            return "[Empty List]"
        cur = self.head
        s = ""
        while cur != None:
            s += f'({cur.value})'
            if cur.next is not None:
                s += '-->'
            cur = cur.next
        return s
    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None
    def delete(self, value):
        cur = self.head
        # Special case of deleting head
        if cur.value == value:
            self.head = cur.next
            return cur
        # General case of deleting internal node
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next
        return None  # If we got here, nothing found
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    def insert_or_overwrite_value(self, value):
        node = self.find(value)
        if node is None:
            # Make a new node
            self.insert_at_head(Node(value))
        else:
            # Overwrite old value
            node.value = value
if __name__ == "__main__":
    l = LinkedList()
    print(l)
    for i in range(5):
        l.insert_at_head(Node(i))
    print(l)
    print(l.delete(2))
    print(l)
    print(l.delete(4))
    print(l)
    print(l.delete(0))
    print(l)
    print(l.find(0))
    print(l.find(3))
    print(l.find(1))
    l.insert_or_overwrite_value(4)
    print(l)
    l.insert_or_overwrite_value(4)
    print(l)


# Load factor/resize notes 

# Hash table load factor
# ----------------------
# Metric to indicate how overfull the hashtable is.
# Lightly-loaded hash table:
# 0 |-> D
# 1 |-> H
# 2 |-> A
# 3 |-> C
# 4 |-> G
# 5 |-> B
# 6 |-> E
# 7 |-> F
# More loaded:
# 0 |-> D -> M
# 1 |-> H
# 2 |-> A -> I
# 3 |-> C -> J -> L -> N
# 4 |-> G
# 5 |-> B -> O
# 6 |-> E -> K -> P
# 7 |-> F
# Way overloaded:
# 0 |-> D -> M -> Q
# 1 |-> H -> R -> X -> Y
# 2 |-> A -> I -> 0
# 3 |-> C -> J -> L -> N -> Z
# 4 |-> G -> S -> U
# 5 |-> B -> O -> 1 -> 2
# 6 |-> E -> K -> P -> W
# 7 |-> F -> T -> V
# How do we know when to resize the hash table?
# load factor = number of elements stored in the hash table / number of slots
# 4 / 8 = 0.5
# 8 / 8 = 1.0
# 16 / 8 = 2.0
# General rules of thumb
# If the load factor is over 0.7, grow the table to keep performance up
# If the load factor is under 0.2, shrink the table (down to some minimum) to
# keep memory consumption down.
# Grow the table: double the size
# Shrink the table: halve the size (down to some minimum)
# Each time you PUT:
#     if the load factor > 0.7:
#         create a new array with double the size of the old one
#         for each element in the old array:
#             PUT in the new array
