#!/usr/bin/env python

list = range(1, 50)
for i in list:
    if i == 13:
        continue
    elif i == 39:
        print i
        break
    else:
        print i

