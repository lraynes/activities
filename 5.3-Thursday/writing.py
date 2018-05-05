import os
import csv

output_path = os.path.join(".", "output", "new.csv")

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["First Name", "Last Name", "SSN"])
    csvwriter.writerow(["Laura", "Raynes", "555-55-5555"])
