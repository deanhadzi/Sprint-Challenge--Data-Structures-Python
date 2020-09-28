# Runtime complexity of this code is O(n^2)

import time
from binary_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#1 Solution using Binary Trees(copied from last week hw).
# Instantiate the Binary Tree with the first item from names_1
binary_tree = BSTNode(names_1[0])
# Iterate through the rest of the names_1 file and add all names to the tree
for name_1 in names_1[1:]:
    binary_tree.insert(name_1)

# Iterate through the names_2 list and check against binary tree.
# If duplicates are found, append them to the duplicate list.
for name_2 in names_2:
    if binary_tree.contains(name_2):
        duplicates.append(name_2)

### TIME RESULT: 0.11 seconds

#2 Solution, using Python built in tools.
#duplicates = list(set(names_1).intersection(names_2))

### TIME RESULT: 0.01 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
