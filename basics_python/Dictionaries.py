"""
Dictionaries
"""

user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

#print(user_dictionary)
#print(user_dictionary.get("username"))

# Adding to dict
#user_dictionary["married"] = True
#print(user_dictionary)

#print(len(user_dictionary))

# Remove from dict
# user_dictionary.pop("age")
# print(user_dictionary)

# Clean dict
#user_dictionary.clear()
#print(user_dictionary)

# Delete the whole dictionary will generate print errors
# del user_dictionary
#print(user_dictionary)

# Loop through dictionary
# Only gets keys
# for x in user_dictionary:
#     print(x)
#
# #Get both key and values in loop
# for x,y in user_dictionary.items():
#     print(x, y)
#

# This removes the age from dict1 too
# user_dictionary2 = user_dictionary
# user_dictionary2.pop("age")
# print(user_dictionary)

# Copies a dictionary with a copy to not alter original
user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary2)
print(user_dictionary)