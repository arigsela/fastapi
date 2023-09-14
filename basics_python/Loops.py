"""
For & while loops
"""

my_list = [1,2,3,4,5]

# Iterate over list,tuple,set,string
# iterator can be anything
# for iterator in my_list:
#     print(iterator)

# Iterate through a range in a list using index
# for x in range(3, 5):
#     print(my_list[x])
#
# sum_of_for_loop = 0
#
# for x in my_list:
#     sum_of_for_loop += x
#
# print(sum_of_for_loop)
#

# my_list_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#
# for x in my_list_str:
#     print(f"Happy {x}!")
#

i = 0

while i < 5:
    i += 1

    # Goes back to beginning of look
    if i == 3:
        continue
    print(i)
    # Stops the loop and exits completely
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

