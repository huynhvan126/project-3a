# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/17/2024
# Description: The min and max of integers input.
print("How many integers would you like to enter?")
number_integers = int(input())
min_value = None
max_value = None
print(f"Please enter {number_integers} integer")
for i in range(number_integers):
    integer = int(input())
    if min_value is None or integer < min_value:
        min_value = integer
    if max_value is None or integer > max_value:
        max_value = integer
print(f"min: {min_value}")
print(f"max: {max_value}")