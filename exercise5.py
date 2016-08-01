#!/usr/bin/env python

#Part 1 - Open a file and read contents
file = open("my_file.txt", "r")
output = file.readlines()
print "File: {}".format("my_file.txt")
for line in output:
    print line.strip()
file.close()

#Part 2 - Create new file
file = open("my_file2.txt", "w")
file.write("This is another file\n")
file.close()
with open("my_file2.txt", "r") as file:
    print "\nFile: {}".format("my_file2.txt")
    for line in file.readlines():
        print line.strip()

#Part 3 - Open my_file2.txt, append something
with open("my_file2.txt", "a") as file:
    file.write("This is a new line.\n")
    file.write("And this too!\n")
with open("my_file2.txt", "r") as file:
    print "\nFile: {} after being appended:\n".format("my_file2.txt")
    for line in file.readlines():
        print line.strip()
