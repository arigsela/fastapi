"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list)
print(my_list[2:4])

people_list = ["Eric", "Adolf", "Jeff"]
print(people_list)

people_list[0] = "Ari"
print(people_list)

# Start at 0 index and end at 2 index (not including)
print(people_list[0:2])

# Add to the end of the list
my_list.append(1000)
print(my_list)

# Add at the second index
my_list.insert(2, 1000)
print(my_list)

# Remove with value of 8
my_list.remove(8)
print(my_list)

# Remove index 0 from the list
my_list.pop(0)
print(my_list)

my_list.sort()
print(my_list)