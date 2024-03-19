#!/usr/bin/env python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if idx is negative or out of range
    else:
        return my_list[:idx] + my_list[idx+1:]
