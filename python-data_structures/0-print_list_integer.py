#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))

# Example usage
my_list = [1, 2, 3]
print_list_integer(my_list)
