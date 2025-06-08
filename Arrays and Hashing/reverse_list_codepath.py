#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'reverse_lst' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def reverse_lst(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right -= 1 
    
    return lst

if __name__ == '__main__':
    input_str = sys.stdin.read().strip()
    # Convert the input string to a list of integers
    input_list = ast.literal_eval(input_str)
    # Reverse the list
    result = reverse_lst(input_list)
    # Print the reversed list
    print(result)