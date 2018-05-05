import os
import csv
csvpath = os.path.join(".", "cereal.csv")


#path for csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvfile)



    fiber_value = 5

    for row in csvreader:
        
        if(float(row[7]) >= fiber_value):
            print(row[0])
