"""
Functions
"""
#
#
# def my_function():
#     print("Inside my function")
#
#
# def print_my_name(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#
#
# def print_color_red():
#     color = "red"
#     print(color)
#
#
# def print_numbers(highest_number, lower_number):
#     print(highest_number)
#     print(lower_number)
#
#
# def multiply_numbers(a, b):
#     return a * b
#
#
# def print_list(list_of_numbers):
#     for x in list_of_numbers:
#         print(x)
#
#
# my_function()
# print_my_name("Ari", "Sela")
#
# color = "Blue"
# print_color_red()
# print(color)
#
# # Passing arguments with argument names
# print_numbers(lower_number=3, highest_number=10)
#
# solution = multiply_numbers(10, 6)
# print(solution)
#
# numbers_list = [1,2,3,4,5]
# print_list(numbers_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)