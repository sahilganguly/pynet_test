#!/usr/bin/env python
string1 = 'Bob'
string2 = 'Dan'
string3 = 'Blob'
print "{:>30} {:>30} {:>30}".format(string1, string2, string3)
string4 = raw_input("Please enter a 4th name: ")
print "{:>30} {:>30} {:>30} {:>30}".format(string1, string2, string3, string4)
