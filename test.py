#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the braces function below.
def braces(values):
    result = []
    for value in values:
        lst = list()
        for each in value:
            if len(lst)==0:
                lst.append(counterpart(each))
            elif lst[-1] != each and each in lst:
                result.append("NO")
                break
            elif lst[-1] != each:
                lst.append(counterpart(each))
            elif lst[-1]==each:
                lst.pop()
        if len(lst)==0:           
            result.append("YES")
    
    return(result)

def counterpart(val):
    if val=="{":
        return "}"
    elif val =="(":
        return ")"
    elif val =="[":
        return "]"

if __name__ == '__main__':
    listtt = ["{[}]}","{}[]()"]
    print(braces(listtt))