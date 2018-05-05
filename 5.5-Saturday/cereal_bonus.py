import os
import csv
csvpath = os.path.join(".", "cereal_bonus.csv")


#path for csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvfile)



    fiber_value = 5

    for row in csvreader:
       
        if(row > 0):
            
            if(float(row[7]) >= fiber_value):
             print(row[0])
