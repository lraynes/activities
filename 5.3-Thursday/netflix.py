#import the csv
import os
import csv
csvpath = os.path.join(".", "Resources","netflix_ratings.csv")


#path for csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvfile)
    
    #user input
    netflix_input = str(input("What movie are you looking for? "))

    #starting value for found
    found = False

    for row in csvreader:
        #if the first string in the list, title, equals the netflix input, then
        if row[0] == netflix_input:
            #print the row
            print(row[0] + " is rated " + row[1])
            #found is now true, we found it
            found = True
            #now that an external condition is met, found=true, you can break out of for loop
            break
    
    if found == False:
        print("nope, sorry")
