"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/27/21
Homework Problem #4_4
Description of Problem: 
Print the keys, values, keys and values as formatted data,
sort by key and print list of tuples for the key/value pairs,
and sort by value and print as formated data for key/value for the given dictionary.
"""
MY_DICT = {'a':15, 'c':18, 'b':20}

keys = list(MY_DICT.keys())
values = list(MY_DICT.values())
val_sort = {k: v for k, v in sorted(MY_DICT.items(), key=lambda item: item[1])}

print("Keys:", keys)
print("Values:", str(values)[1:-1])
print("Key value pairs:", ', '.join('%s: %s' % (k,MY_DICT[k]) for k in MY_DICT.keys()))
print("Key value pairs ordered by key:", list(tuple(sorted(MY_DICT.items()))))
print("Key value pairs ordered by value:", ', '.join('%s: %s' % (k,val_sort[k]) for k in val_sort.keys()))
