import random
import string

print(string.ascii_letters)

for x in range(10):
    print(random.randint(1,10))

rand = random.randint(1,10)
print(rand)

import os
import csv

csvpath = os.path.join(".", "Resources","accounting.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvfile)
    for row in csvreader:
        print(row)