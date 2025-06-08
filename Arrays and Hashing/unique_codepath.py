#!/bin/python3

import math
import os
import random
import re
import sys



def has_all_unique_characters(s):
    # Write your code here
    
    cDict = {}
    
    for c in s:
        if c in cDict:
            return False
        cDict[c] = 1
    
    return True
    
    
if __name__ == "__main__":